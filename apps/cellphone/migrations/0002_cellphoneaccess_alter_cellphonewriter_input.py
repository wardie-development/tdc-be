# Generated by Django 5.0 on 2023-12-09 02:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cellphone", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CellphoneAccess",
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
                ("whatsapp", models.CharField(max_length=255, verbose_name="Whatsapp")),
                (
                    "password",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Senha"
                    ),
                ),
                (
                    "valid_until",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Válido até"
                    ),
                ),
                (
                    "days_to_expire",
                    models.IntegerField(verbose_name="Dias para expirar"),
                ),
            ],
            options={
                "verbose_name": "Acesso",
                "verbose_name_plural": "Acessos",
            },
        ),
        migrations.AlterField(
            model_name="cellphonewriter",
            name="input",
            field=models.TextField(
                help_text="\nEscreva aqui no seguinte formato: <br>\n<b>Marca Modelo</b>: Marca Modelo - Marca Modelo - Marca Modelo <br>\n<b>Marca Modelo</b>: Marca Modelo - Marca Modelo - Marca Modelo <br>\n<br><br>\nCaso a compatibilidade tenha a mesma marca, não é necessário incluir \na marca na compatibilidade, desta forma: <br>\n<b>MarcaX</b> ModeloX: ModeloX - ModeloX - <b>MarcaY</b> ModeloY \n            ",
                verbose_name="Entrada",
            ),
        ),
    ]
