# Generated by Django 5.0 on 2023-12-16 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cellphone", "0014_cellphoneaccess_client_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cellphoneaccess",
            name="days_to_expire",
            field=models.CharField(
                choices=[
                    ("3", "3 dias"),
                    ("30", "30 dias"),
                    ("90", "90 dias"),
                    ("180", "180 dias"),
                ],
                default="3",
                max_length=255,
                verbose_name="Dias para expirar",
            ),
        ),
    ]