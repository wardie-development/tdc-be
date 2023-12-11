from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.cellphone.models import Brand, Cellphone, CellphoneWriter, CellphoneAccess, \
    CellphoneSuggestion


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "is_active"]
    search_fields = ["name"]


@admin.register(Cellphone)
class CellphoneAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "is_active"]
    search_fields = ["name"]
    filter_horizontal = ["cellphone_screen_protector_compatibilities"]


@admin.register(CellphoneWriter)
class CellphoneWriterAdmin(admin.ModelAdmin):
    list_display = ["created_at", "updated_at", "is_active"]
    search_fields = ["input"]


@admin.register(CellphoneAccess)
class CellphoneAccessAdmin(admin.ModelAdmin):
    list_display = ["formatted_whatsapp", "created_at", "valid_until", "is_access_expired", "send_whatsapp_message"]
    search_fields = ["whatsapp"]
    fieldsets = (
        ("Criar Acesso", {"fields": ("whatsapp", "days_to_expire", "password")}),
    )
    actions = ["renew_access"]
    readonly_fields = ["password"]

    @staticmethod
    def send_whatsapp_message(access):
        whatsapp_link = access.whatsapp_message_link
        return mark_safe(
            "<a "
            'class="btn btn-high btn-success" '
            'target="_blank" '
            f'href="{whatsapp_link}">'
            f'<img src="https://static-00.iconduck.com/assets.00/whatsapp-icon-2040x2048-8b5th74o.png" width=50/>'
            'Mandar mensagem no whatsapp'
            "</a>"
        )

    send_whatsapp_message.short_description = "Enviar mensagem no whatsapp"

    def renew_access(self, _request, queryset):
        for access in queryset:
            access.renew_access()
            access.save()

    renew_access.short_description = "Renovar acesso"


@admin.register(CellphoneSuggestion)
class CellphoneSuggestionAdmin(admin.ModelAdmin):
    list_display = ["name", "whatsapp", "suggestion", "created_at", "is_active"]
    search_fields = ["name", "whatsapp", "suggestion"]
    fieldsets = (
        ("Criar Sugestão", {"fields": ("name", "whatsapp", "suggestion")}),
    )
    readonly_fields = ["name", "whatsapp", "suggestion"]
