# Generated by Django 5.0 on 2023-12-09 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Marca",
                "verbose_name_plural": "Marcas",
            },
        ),
        migrations.CreateModel(
            name="CellphoneWriter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "input",
                    models.TextField(
                        help_text="Escreva aqui no seguinte formato: \nMarca Modelo: Marca Modelo, Marca Modelo, Marca Modelo \nMarca Modelo: Marca Modelo, Marca Modelo, Marca Modelo \n\n\nCaso a compatibilidade tenha a mesma marca, não é necessário incluir a marca na compatibilidade, desta forma: \nMarcaX ModeloX: ModeloX, ModeloX, MarcaY ModeloY ",
                        verbose_name="Entrada",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cadastrador de celulares",
                "verbose_name_plural": "Cadastrador de celulares",
            },
        ),
        migrations.CreateModel(
            name="Cellphone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("model", models.CharField(max_length=255, verbose_name="Modelo")),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cellphone.brand",
                        verbose_name="Marca",
                    ),
                ),
                (
                    "cellphone_screen_protector_compatibilities",
                    models.ManyToManyField(
                        blank=True,
                        to="cellphone.cellphone",
                        verbose_name="Compatibilidades com películas",
                    ),
                ),
            ],
            options={
                "verbose_name": "Celular",
                "verbose_name_plural": "Celulares",
                "ordering": ["model"],
            },
        ),
    ]
