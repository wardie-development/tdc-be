# Generated by Django 5.0 on 2023-12-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cellphone", "0021_cellphoneaccess_access_limit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cellphoneaccess",
            name="is_test_access",
            field=models.BooleanField(default=False, verbose_name="É acesso de teste?"),
        ),
    ]