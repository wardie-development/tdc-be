from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.orderlist.models import CellphoneModel, Order


@admin.register(CellphoneModel)
class CellphoneModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "whatsapp", "send_whatsapp_message", "message", "models", "access_pdf_button")
    search_fields = ("name", "whatsapp", "message")
    readonly_fields = ("name", "whatsapp", "message", "models", "access_pdf_button", "send_whatsapp_message")
    list_display_links = ("name", "whatsapp", "message")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "send_whatsapp_message",
                    "access_pdf_button",
                    "name",
                    "whatsapp",
                    "message",
                    "models",
                )
            },
        ),
    )

    def models(self, obj):
        return mark_safe(f"""
        <table>
            <thead>
                <tr>
                    <th>Modelo</th>
                    <th>Películas</th>
                    <th>Capinhas</th>
                </tr>
            </thead>
            <tbody>
                {"".join([
                    f'''
                    <tr>
                        <td>{model.cellphone_model.name}</td>
                        <td>{model.screen_protectors}</td>
                        <td>{model.cases}</td>
                    </tr>
                    ''' for model in obj.cellphone_models.all()
                ])}
            </tbody>
        </table>
        """)

    def access_pdf_button(self, obj):
        style = "display: inline-block; background-color: #417690; color: #fff; padding: 5px; border-radius: 5px; text-decoration: none; width: 25px; height: 25px; display: flex; justify-content: center; align-items: center"
        return mark_safe(
            f"""
                <a 
                    style="{style}"
                    href="{obj.pdf_link}"
                    target="_blank"
                >
                   PDF
                </a>
            """
        )

    def send_whatsapp_message(self, order):
        whatsapp_link = order.whatsapp_message_link
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
                    Entrar em contato
                </a>
            </div>
            """
        )

    send_whatsapp_message.short_description = "Whatsapp"
    access_pdf_button.short_description = "PDF"
    models.short_description = "Modelos"
