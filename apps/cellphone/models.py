import uuid
from datetime import timedelta
from typing import List

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from apps.base.base_model import BaseModel
from apps.user.models import User


class Brand(BaseModel):
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(verbose_name="Ordem", default=0, null=True,
                                        blank=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.name

    mapped_colors = {
        "Samsung": "#2459AA",
        "Motorola": "#d10305",
        "Xiaomi": "#f85e12",
        "Apple": "#414c65",
        "LG": "#1a9d68",
        "Asus": "#655241",
        "Oppo": "#23998b",
    }


class CellphoneAccess(BaseModel):
    client = models.CharField(max_length=255, verbose_name="Cliente", null=True, blank=True)
    whatsapp = models.CharField(max_length=255, verbose_name="Whatsapp")
    password = models.CharField(
        max_length=255, verbose_name="Senha", null=True, blank=True
    )
    valid_until = models.DateTimeField(verbose_name="Válido até", null=True, blank=True)
    days_to_expire = models.CharField(
        verbose_name="Dias para expirar", max_length=255, choices=[
            ("3", "3 dias"),
            ("30", "30 dias"),
            ("90", "90 dias"),
            ("180", "180 dias"),
        ],
        default="3"
    )
    is_test_access = models.BooleanField(
        verbose_name="É acesso de teste?", default=True
    )

    class Meta:
        verbose_name = "Acesso"
        verbose_name_plural = "Acessos"

    def __str__(self):
        return self.whatsapp

    @property
    def whatsapp_message(self):
        whatsapp_line_break = "%0a"
        return f"""
_Agora você é um(a) Cliente PLUS da TDC!_{whatsapp_line_break}{whatsapp_line_break}
A sua senha de acesso para a página *Tabela de Películas [PLUS]* é: *{self.password}*{whatsapp_line_break}{whatsapp_line_break}
Link de acesso:{whatsapp_line_break}https://app.tecnicosdecelular.com.br/tabela-plus/{whatsapp_line_break}{whatsapp_line_break}
Sua senha é válida até:{whatsapp_line_break}*{self.valid_until.strftime("%d/%m/%Y às %H:%M")}h*
            """

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.renew_access()
        super().save(*args, **kwargs)

    def renew_access(self):
        self.valid_until = timezone.now() + timedelta(days=int(self.days_to_expire))
        if self.password is None:
            self.password = User.objects.make_random_password(length=6).lower()

    def is_access_expired(self):
        return self.valid_until < timezone.now()

    @property
    def whatsapp_message_link(self):
        whatsapp_link = "https://api.whatsapp.com/send"
        return (
            f"{whatsapp_link}?phone=55{self.whatsapp}" f"&text={self.whatsapp_message}"
        )


class Cellphone(BaseModel):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, verbose_name="Marca", related_name="cellphones", db_index=True
    )
    model = models.CharField(max_length=255, verbose_name="Modelo")
    compatibility_line = models.CharField(
        max_length=255, verbose_name="Linha de compatibilidade", null=True, blank=True
    )
    is_visible_for_test = models.BooleanField(
        verbose_name="É visível para testes?", default=False
    )
    news_views = models.ManyToManyField(
        CellphoneAccess, verbose_name="Visualizações de novidades", blank=True
    )
    scheduled_to = models.DateField(
        verbose_name="Agendado para", null=True, blank=True
    )

    class Meta:
        verbose_name = "Celular"
        verbose_name_plural = "Celulares"
        ordering = ["model"]

    @property
    def name(self):
        return self.model

    @property
    def brand_name(self):
        return self.brand.name

    @property
    def is_visible(self):
        _is_visible = self.scheduled_to is None or self.scheduled_to <= timezone.localdate()
        return "Visível" if _is_visible else f"Visível a partir de {self.scheduled_to.strftime('%d/%m/%Y')}"

    def __str__(self):
        return self.name

    def to_representation(self):
        return {
            "brand": self.brand.name,
            "model": self.model,
            "compatibilities": self.compatibility_line,
        }


class CellphoneWriter(BaseModel):
    UPDATE_STRING = "ATUALIZAR"
    ADD_STRING = "ADICIONAR"
    REMOVE_STRING = "REMOVER"

    input = models.TextField(
        verbose_name="Entrada",
        help_text=(
            f"""
Siga rigorosamente este formato: <br>
<br>
{UPDATE_STRING}:

<br>
Marca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>
Marca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>

<br>

{ADD_STRING}:

<br>
Marca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>
Marca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>

<br>

{REMOVE_STRING}:

<br>
Marca Modelo<br>
Marca Modelo<br>

<br>

<hr class="solid">

Opcionalmente, você pode colocar no final de cada linha de ação, uma data que queira que seja publicada aquele celular, Exemplo: <br>

<br>

Marca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3 [dd/mm/YYYY]<br>
            """
        ),
    )

    def clean(self):
        try:
            actions = self._get_actions()

            for action, cellphones in actions.items():
                formatted_action = action.replace(":", "")
                if formatted_action == self.UPDATE_STRING:
                    self._update_cellphones(cellphones)
                elif formatted_action == self.ADD_STRING:
                    self._add_cellphones(cellphones)
                elif formatted_action == self.REMOVE_STRING:
                    self._remove_cellphones(cellphones)
        except Exception as e:
            raise ValidationError("Verifique se o formato está correto")

    @staticmethod
    def _parse_line(line):
        brand_model, compatibilities = line.split(":")
        main_cellphone = brand_model.split()
        brand = main_cellphone[0]
        date = line[-12:]
        has_schedule = date[0] == "[" and date[-1] == "]"

        scheduled_to = timezone.now()
        model = " ".join(main_cellphone[1:])
        if has_schedule:
            compatibilities = compatibilities.replace(date, "")
            date = date.replace("[", "").replace("]", "")
            day, month, year = date.split("/")
            scheduled_to = f"{year}-{month}-{day}"

        return brand, model, compatibilities, scheduled_to

    @staticmethod
    def _make_cellphone(compatibility):
        splitted_compatibility = compatibility.split()
        brand = splitted_compatibility[0]
        model = " ".join(splitted_compatibility[1:])

        return Cellphone.objects.get_or_create(
            brand=Brand.objects.get_or_create(name=brand)[0], model=model
        )[0]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.delete()

    class Meta:
        verbose_name = "Cadastrador de celulares"
        verbose_name_plural = "Cadastrador de celulares"

    def __str__(self):
        return "Cadastrador de celulares"

    def _get_actions(self):
        lines = [
            line for line in self.input.splitlines()
            if line != ""
        ]

        cellphones = {
            f"{self.UPDATE_STRING}:": [],
            f"{self.ADD_STRING}:": [],
            f"{self.REMOVE_STRING}:": [],
        }

        actions = list(cellphones.keys())
        action = actions[0]

        for line in lines:
            if line in actions:
                action = line
            else:
                cellphones[action].append(line.replace("<br>", ""))

        return cellphones

    def _update_cellphones(self, cellphones: List[str]):
        for line in cellphones:
            brand, model, compatibilities, scheduled_to = self._parse_line(line)

            cellphone = Cellphone.objects.get_or_create(
                brand__name=brand, model=model
            )[0]
            cellphone.scheduled_to = scheduled_to
            cellphone.compatibility_line = compatibilities
            cellphone.save()

    def _add_cellphones(self, cellphones):
        for line in cellphones:
            brand, model, compatibilities, scheduled_to = self._parse_line(line)
            cellphone = Cellphone.objects.get_or_create(
                brand=Brand.objects.get_or_create(name=brand)[0],
                model=model
            )[0]

            cellphone.scheduled_to = scheduled_to
            cellphone.compatibility_line = compatibilities
            cellphone.save()

    @staticmethod
    def _remove_cellphones(cellphones):
        for line in cellphones:
            splitted_line = line.split()
            brand = splitted_line[0]
            model = " ".join(splitted_line[1:])
            cellphone = Cellphone.objects.get(brand__name=brand, model=model)
            cellphone.delete()


class CellphoneAccessToken(BaseModel):
    access = models.ForeignKey(
        CellphoneAccess,
        on_delete=models.CASCADE,
        verbose_name="Acesso",
        related_name="tokens",
    )
    token = models.CharField(max_length=255, verbose_name="Token")

    class Meta:
        verbose_name = "Token de acesso"
        verbose_name_plural = "Tokens de acesso"

    def __str__(self):
        return self.token

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def renew_token_if_expired(self):
        if self.is_expired:
            self.token = uuid.uuid4().hex
            self.created_at = timezone.now()
            self.save()

    @property
    def is_expired(self):
        hours = 1
        is_expired = self.created_at + timedelta(hours=hours) < timezone.now()
        return is_expired


class CellphoneSuggestion(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Nome")
    whatsapp = models.CharField(max_length=255, verbose_name="Whatsapp")
    suggestion = models.TextField(verbose_name="Sugestão")

    class Meta:
        verbose_name = "Sugestão"
        verbose_name_plural = "Sugestões"

    def __str__(self):
        return f"Sugestão de {self.name}"
