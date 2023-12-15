from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.cellphone.models import (
    Brand,
    Cellphone,
    CellphoneWriter,
    CellphoneAccess,
    CellphoneSuggestion,
)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "is_active"]
    search_fields = ["name"]


@admin.register(Cellphone)
class CellphoneAdmin(admin.ModelAdmin):
    list_display = ["brand_name", "model", "created_at", "is_active", "is_visible"]
    search_fields = ["model", "brand__name", "cellphone_screen_protector_compatibilities__model"]
    filter_horizontal = ["cellphone_screen_protector_compatibilities"]
    fields = [
        "brand",
        "model",
        "cellphone_screen_protector_compatibilities",
        "is_main",
        "scheduled_to"
    ]
    list_display_links = ["brand_name", "model"]
    list_per_page = 10
    list_filter = ["is_main", "is_active", "brand__name", "scheduled_to"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("brand")


@admin.register(CellphoneWriter)
class CellphoneWriterAdmin(admin.ModelAdmin):
    list_display = ["created_at", "updated_at", "is_active"]
    search_fields = ["input"]
    fields = [
        "input",
    ]


@admin.register(CellphoneAccess)
class CellphoneAccessAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "password",
        "send_whatsapp_message",
        "valid_until",
        "status",
        "edit",
        "delete"
    ]
    search_fields = ["whatsapp", "client", "password"]
    fieldsets = (
        ("Criar Acesso", {"fields": ("client", "whatsapp", "days_to_expire", "password")}),
    )
    actions = ["renew_access"]
    list_display_links = ["client", "password"]
    list_filter = ["days_to_expire", "created_at", "valid_until"]
    list_per_page = 10

    @staticmethod
    def send_whatsapp_message(access):
        whatsapp_link = access.whatsapp_message_link
        send_message_icon = "https://beeluvd.eu/wp-content/uploads/2014/09/send-icon-white.png"
        whatsapp_icon = "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/whatsapp-white-icon.png"
        button_style = "display: inline-block; background-color: #23a455; color: #fff; padding-inline: 10px; padding-block: 5px; border-radius: 5px; text-decoration: none; margin-inline: 10px;"
        return mark_safe(
            f"""
            <div>
                <a
                    style="{button_style}"
                    target="_blank"
                    href="https://api.whatsapp.com/send?phone=55{access.whatsapp}"
                >
                    <img src="{whatsapp_icon}" width=15/>
                    Chamar
                </a>
                <a
                    style="{button_style}"
                    target="_blank"
                    href="{whatsapp_link}"
                >
                    <img src="{send_message_icon}" width=15/>
                    Enviar
                </a>
            </div>
            """
        )

    send_whatsapp_message.short_description = "Whatsapp"

    def renew_access(self, _request, queryset):
        for access in queryset:
            access.renew_access()
            access.save()

    renew_access.short_description = "Renovar acesso"

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
class CellphoneSuggestionAdmin(admin.ModelAdmin):
    list_display = ["name", "whatsapp", "suggestion", "created_at", "is_active"]
    search_fields = ["name", "whatsapp", "suggestion"]
    fieldsets = (("Criar Sugestão", {"fields": ("name", "whatsapp", "suggestion")}),)
    readonly_fields = ["name", "whatsapp", "suggestion"]
