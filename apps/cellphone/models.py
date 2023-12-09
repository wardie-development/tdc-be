from datetime import timedelta

from django.db import models
from django.utils import timezone

from apps.base.base_model import BaseModel
from apps.user.models import User


class Brand(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.name


class Cellphone(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Marca")
    model = models.CharField(max_length=255, verbose_name="Modelo")
    cellphone_screen_protector_compatibilities = models.ManyToManyField(
        "self",
        verbose_name="Compatibilidades com películas",
        blank=True
    )

    class Meta:
        verbose_name = "Celular"
        verbose_name_plural = "Celulares"
        ordering = ["model"]

    @property
    def name(self):
        return f"{self.brand.name} {self.model}"

    def __str__(self):
        return self.name


class CellphoneWriter(BaseModel):
    input = models.TextField(
        verbose_name="Entrada",
        help_text=(
            """
Escreva aqui no seguinte formato: <br>
<b>Marca Modelo</b>: Marca Modelo - Marca Modelo - Marca Modelo <br>
<b>Marca Modelo</b>: Marca Modelo - Marca Modelo - Marca Modelo <br>
<br><br>
Caso a compatibilidade tenha a mesma marca, não é necessário incluir 
a marca na compatibilidade, desta forma: <br>
<b>MarcaX</b> ModeloX: ModeloX - ModeloX - <b>MarcaY</b> ModeloY 
            """
        )
    )

    def update_cellphones(self):
        for line in self.input.splitlines():
            brand, model, compatibilities = self._parse_line(line)

            brand = Brand.objects.get_or_create(name=brand)[0]
            cellphone = Cellphone.objects.get_or_create(
                brand=brand,
                model=model
            )[0]

            cellphone.cellphone_screen_protector_compatibilities.set(compatibilities)
            cellphone.save()

        self.delete()

    def _parse_line(self, line):
        brand_model, compatibilities = line.split(":")
        brand, model = brand_model.split()

        compatibilities = compatibilities.split(" - ")

        compatibilities = [
            self._make_cellphone(brand, compatibility)
            for compatibility in compatibilities
        ]

        return brand, model, compatibilities

    @staticmethod
    def _make_cellphone(cellphone_brand, compatibility):
        splitted_compatibility = compatibility.split()
        brand = cellphone_brand
        model = splitted_compatibility[0]

        if len(splitted_compatibility) == 2:
            brand = splitted_compatibility[0]
            model = splitted_compatibility[1]

        return Cellphone.objects.get_or_create(
            brand=Brand.objects.get_or_create(name=brand)[0],
            model=model
        )[0]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_cellphones()

    class Meta:
        verbose_name = "Cadastrador de celulares"
        verbose_name_plural = "Cadastrador de celulares"

    def __str__(self):
        return "Cadastrador de celulares"


class CellphoneAccess(BaseModel):
    whatsapp = models.CharField(max_length=255, verbose_name="Whatsapp")
    password = models.CharField(max_length=255, verbose_name="Senha", null=True, blank=True)
    valid_until = models.DateTimeField(verbose_name="Válido até", null=True, blank=True)
    days_to_expire = models.PositiveIntegerField(verbose_name="Dias para expirar", default=30)

    class Meta:
        verbose_name = "Acesso"
        verbose_name_plural = "Acessos"

    def __str__(self):
        return self.whatsapp

    @property
    def whatsapp_message(self):
        return f"""
        _Agora você é um(a) Cliente PLUS da TDC!_
        
        A sua senha de acesso para a página *Tabela de Películas [PLUS]* é: *{self.password}*
        
        Link de acesso:
        https://app.tecnicosdecelular.com.br/tabela-plus/
        
        Sua senha é valida até:
        *{self.valid_until.strftime("%d/%m/%Y")} às {self.valid_until.strftime("%H:%M")}h*
        """

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.renew_access()
        super().save(*args, **kwargs)

    def renew_access(self):
        self.valid_until = timezone.now() + timedelta(days=self.days_to_expire)
        if self.password is None:
            self.password = User.objects.make_random_password(length=6).lower()

    def is_access_expired(self):
        return self.valid_until < timezone.now()

    @property
    def whatsapp_message_link(self):
        whatsapp_link = "https://api.whatsapp.com/send"
        return (
            f"{whatsapp_link}?phone=55{self.whatsapp}"
            f"&text={self.whatsapp_message}"
        )

    @property
    def formatted_whatsapp(self):
        return f"({self.whatsapp[:2]}) {self.whatsapp[2:7]}-{self.whatsapp[7:]}"
