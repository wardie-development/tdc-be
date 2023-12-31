from datetime import timedelta

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path
from django.utils import timezone
from django.utils.safestring import mark_safe

from apps.cellphone.models import (
    Brand,
    Cellphone,
    CellphoneWriter,
    CellphoneAccess,
    CellphoneSuggestion, CellphoneAccessLog, CellphoneAccessTry,
)


class AccessControlMixin:
    def get_list_filter(self, request):
        list_filter = super().get_list_filter(request)
        if request.user.is_staff and not request.user.is_superuser:
            return []
        return list_filter


@admin.register(Brand)
class BrandAdmin(AccessControlMixin, admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "is_active"]
    search_fields = ["name"]


@admin.register(Cellphone)
class CellphoneAdmin(AccessControlMixin, admin.ModelAdmin):
    list_display = ["brand_name", "model", "compatibility_line", "is_visible_for_test", "is_active"]
    search_fields = ["model", "brand__name", "compatibility_line"]
    fields = [
        "brand",
        "model",
        "compatibility_line",
        "is_visible_for_test",
        "scheduled_to"
    ]
    list_display_links = ["brand_name", "model"]
    list_per_page = 10
    list_filter = ["is_active", "brand__name", "scheduled_to", "is_visible_for_test"]
    actions = ["make_visible_for_test", "make_invisible_for_test"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("brand")

    def make_visible_for_test(self, _request, queryset):
        queryset.update(is_visible_for_test=True)

    make_visible_for_test.short_description = "Tornar visível para teste"

    def make_invisible_for_test(self, _request, queryset):
        queryset.update(is_visible_for_test=False)

    make_invisible_for_test.short_description = "Tornar invisível para teste"


@admin.register(CellphoneWriter)
class CellphoneWriterAdmin(AccessControlMixin, admin.ModelAdmin):
    list_display = ["created_at", "updated_at", "is_active"]
    search_fields = ["input"]
    fields = [
        "input",
    ]


class CellphoneAccessLogInline(admin.TabularInline):
    model = CellphoneAccessLog
    extra = 0
    readonly_fields = ["ip", "user_agent", "token", "created_at"]
    fields = ["ip", "user_agent", "token", "created_at"]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(CellphoneAccess)
class CellphoneAccessAdmin(AccessControlMixin, admin.ModelAdmin):
    change_list_template = "admin/cellphone/change_list.html"
    list_display = [
        "client",
        "password",
        "send_whatsapp_message",
        "created_at",
        "valid_until",
        "status",
        "is_plus_access",
        "edit",
        "delete"
    ]
    search_fields = ["whatsapp", "client", "password"]
    fieldsets = (
        ("Criar Acesso", {"fields": ("client", "whatsapp", "is_plus_access", "days_to_expire", "access_limit", "password", "valid_until")}),
    )
    actions = ["renew_access", "renew_to_30_days", "renew_to_90_days", "renew_to_180_days"]
    list_display_links = ["client", "password"]
    list_filter = ["was_converted", "days_to_expire", "valid_until", "is_plus_access"]
    list_per_page = 10
    inlines = [CellphoneAccessLogInline]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create-test-access/', self.admin_site.admin_view(self.create_test_access), name='create-test-access'),
        ]
        return custom_urls + urls

    @staticmethod
    def create_test_access(request):
        if request.method == 'POST':

            data = request.POST
            whatsapp = data.get('whatsapp_number')

            if whatsapp:
                access = CellphoneAccess.objects.create(
                    client=f"Cliente - {whatsapp}",
                    whatsapp=whatsapp,
                    is_plus_access=False,
                    days_to_expire="3"
                )
                access.save()

                messages.success(request, f'Acesso de teste criado com sucesso: {whatsapp} {access.password}')
                script = f"""
                <script>
                    window.open('{access.whatsapp_message_link}', '_blank');
                    setTimeout(() => window.location.href = '../', 1000);
                </script>
                """
                return HttpResponse(script)

        return HttpResponseRedirect("../")

    @staticmethod
    def send_whatsapp_message(access):
        whatsapp_link = access.whatsapp_message_link
        send_message_icon = "https://beeluvd.eu/wp-content/uploads/2014/09/send-icon-white.png"
        button_style = "display: inline-block; background-color: #23a455; color: #fff; padding-inline: 10px; padding-block: 5px; border-radius: 5px; text-decoration: none; margin-inline: 10px;"
        return mark_safe(
            f"""
            <div>
                <a
                    style="{button_style}"
                    target="_blank"
                    href="{whatsapp_link}"
                >
                    <img src="{send_message_icon}" width=15/>
                    Enviar Acesso
                </a>
            </div>
            """
        )

    send_whatsapp_message.short_description = "Whatsapp"

    def renew_access(self, _request, queryset):
        for access in queryset:
            access.renew_access()
            access.save()

    def renew_to_30_days(self, _request, queryset):
        self.renew_to(queryset, 30)

    def renew_to_90_days(self, _request, queryset):
        self.renew_to(queryset, 90)

    def renew_to_180_days(self, _request, queryset):
        self.renew_to(queryset, 180)

    renew_access.short_description = "Renovar acesso"
    renew_to_30_days.short_description = "Renovação +30 dias"
    renew_to_90_days.short_description = "Renovação +90 dias"
    renew_to_180_days.short_description = "Renovação +180 dias"

    @staticmethod
    def renew_to(queryset, days):
        for access in queryset:
            access.days_to_expire = str(days)
            access.valid_until = timezone.now() + timedelta(days=days)
            access.was_converted = True
            access.is_plus_access = True
            access.save()

    # Put "remove access" action at last position:
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            actions["delete_selected"][0].short_description = "Remover acessos"
            delete_selected = actions.pop("delete_selected")
            actions["delete_selected"] = delete_selected
        return actions

    def edit(self, obj):
        edit_icon = "https://static-00.iconduck.com/assets.00/edit-icon-255x256-xzgn811y.png"
        style = "display: inline-block; background-color: #417690; color: #fff; padding: 5px; border-radius: 5px; text-decoration: none; width: 25px; height: 25px; display: flex; justify-content: center; align-items: center"
        return mark_safe(
            f"""
                <a 
                    style="{style}"
                    href="/admin/cellphone/cellphoneaccess/{obj.id}/change/"
                >
                    <img src="{edit_icon}" width=15/>
                </a>
            """
        )

    def delete(self, obj):
        delete_icon = """
            <svg fill="#fff" width="15px" height="15px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;"><path d="M11,4.5l10,0c0.828,-0 1.5,-0.672 1.5,-1.5c-0,-0.828 -0.672,-1.5 -1.5,-1.5l-10,0c-0.828,-0 -1.5,0.672 -1.5,1.5c-0,0.828 0.672,1.5 1.5,1.5Z"/><path d="M5,9.5l0,16.5c0,2.761 2.239,5 5,5l12,0c2.761,0 5,-2.239 5,-5l0,-16.5l1.645,0c0.748,-0 1.355,-0.672 1.355,-1.5c-0,-0.828 -0.607,-1.5 -1.355,-1.5l-25.29,0c-0.748,-0 -1.355,0.672 -1.355,1.5c-0,0.828 0.607,1.5 1.355,1.5l1.645,0Zm7,3.5l0,12c-0,0.552 0.448,1 1,1c0.552,0 1,-0.448 1,-1l0,-12c-0,-0.552 -0.448,-1 -1,-1c-0.552,0 -1,0.448 -1,1Zm6,-0l0,12c0,0.552 0.448,1 1,1c0.552,-0 1,-0.448 1,-1l0,-12c0,-0.552 -0.448,-1 -1,-1c-0.552,-0 -1,0.448 -1,1Z"/></svg>
        """
        style = "display: inline-block; background-color: #ba2121; color: #fff; padding: 5px; border-radius: 5px; text-decoration: none; width: 25px; height: 25px; display: flex; justify-content: center; align-items: center"
        return mark_safe(
            f"""
                        <a 
                            style="{style}"
                            href="/admin/cellphone/cellphoneaccess/{obj.id}/delete/"
                        >
                            {delete_icon}
                        </a>
                    """
        )

    @staticmethod
    def status(access):
        status, color = ("EXPIRADA", "#fcdf00") if access.is_access_expired() else ("ATIVA", "#23a455")
        element_style = f"display: inline-block; background-color: {color}; color: #fff; padding-inline: 20px; padding-block: 5px; border-radius: 5px;"
        return mark_safe(f"""
        <div style="{element_style}">
                {status}
        </div>
        """)

    status.short_description = "Status"


@admin.register(CellphoneSuggestion)
class CellphoneSuggestionAdmin(AccessControlMixin, admin.ModelAdmin):
    list_display = ["name", "whatsapp", "suggestion", "created_at", "is_active"]
    search_fields = ["name", "whatsapp", "suggestion"]
    fieldsets = (("Criar Sugestão", {"fields": ("name", "whatsapp", "suggestion")}),)
    readonly_fields = ["name", "whatsapp", "suggestion"]


@admin.register(CellphoneAccessTry)
class CellphoneAccessTryAdmin(AccessControlMixin, admin.ModelAdmin):
    list_display = ["ip", "user_agent", "password_tryed", "created_at"]
    search_fields = ["ip", "user_agent", "password_tryed"]
    readonly_fields = ["ip", "user_agent", "password_tryed", "created_at"]
    list_filter = ["created_at"]
    list_per_page = 10
