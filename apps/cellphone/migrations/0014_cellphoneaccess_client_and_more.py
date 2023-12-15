# Generated by Django 5.0 on 2023-12-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "cellphone",
            "0013_alter_cellphone_cellphone_screen_protector_compatibilities",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="cellphoneaccess",
            name="client",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Cliente"
            ),
        ),
        migrations.AlterField(
            model_name="cellphoneaccess",
            name="days_to_expire",
            field=models.CharField(
                choices=[
                    ("3", "3 dia"),
                    ("30", "30 dias"),
                    ("90", "90 dias"),
                    ("180", "180 dias"),
                ],
                max_length=255,
                verbose_name="Dias para expirar",
            ),
        ),
    ]