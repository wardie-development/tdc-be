# Generated by Django 5.0 on 2023-12-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cellphone", "0019_cellphoneaccesslog"),
    ]

    operations = [
        migrations.CreateModel(
            name="CellphoneAccessTry",
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
                    "password_tryed",
                    models.CharField(max_length=255, verbose_name="Senha tentada"),
                ),
                ("ip", models.CharField(max_length=255, verbose_name="IP")),
                ("user_agent", models.TextField(verbose_name="Agente")),
            ],
            options={
                "verbose_name": "Tentativa de acesso negada",
                "verbose_name_plural": "Tentativas de acesso negadas",
            },
        ),
        migrations.AlterField(
            model_name="cellphoneaccesslog",
            name="user_agent",
            field=models.TextField(verbose_name="Agente"),
        ),
    ]
