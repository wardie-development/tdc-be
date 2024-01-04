from django.db import models

from apps.base.base_model import BaseModel


class CellphoneModel(BaseModel):
    name = models.CharField("Modelo", max_length=255, unique=True)

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    def __str__(self):
        return self.name


class CellphoneModelLine(BaseModel):
    cellphone_model = models.ForeignKey(
        CellphoneModel, on_delete=models.CASCADE, related_name="model_line"
    )
    screen_protectors = models.PositiveIntegerField("Películas")
    cases = models.PositiveIntegerField("Capinhas")

    class Meta:
        verbose_name = "Linha de Modelo"
        verbose_name_plural = "Linhas de Modelo"

    def __str__(self):
        return self.cellphone_model.name


class Order(BaseModel):
    name = models.CharField("Nome", max_length=255)
    whatsapp = models.CharField("Whatsapp", max_length=255)
    message = models.TextField("Mensagem", null=True, blank=True)
    cellphone_models = models.ManyToManyField(
        CellphoneModelLine, related_name="orders", verbose_name="Modelos"
    )

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return self.name

    @property
    def pdf_link(self):
        return f"https://api.tecnicosdecelular.com.br/orders/{self.pk}/pdf/"

    @property
    def whatsapp_message(self):
        whatsapp_line_break = "%0a"
        cellphone_lines = f"{whatsapp_line_break}".join([
            (
                f"*{model.cellphone_model.name}* - Películas: {model.screen_protectors} - Capinhas: {model.cases}"
            ) for model in self.cellphone_models.all()
        ])

        return (
            f"Olá, {self.name}!{whatsapp_line_break}"
            f"Estou entrando em contato pois gostaria de tratar sobre o seu pedido: {whatsapp_line_break}"
            f"{cellphone_lines}"
        )

    @property
    def whatsapp_message_link(self):
        whatsapp_link = "https://api.whatsapp.com/send"
        return (
            f"{whatsapp_link}?phone=55{self.whatsapp}&text={self.whatsapp_message}"
        )
