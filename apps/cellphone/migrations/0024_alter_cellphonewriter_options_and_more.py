# Generated by Django 5.0 on 2024-01-04 01:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cellphone", "0023_alter_cellphoneaccess_days_to_expire"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cellphonewriter",
            options={
                "verbose_name": "Cadastro de celulares",
                "verbose_name_plural": "Cadastro de celulares",
            },
        ),
        migrations.AlterField(
            model_name="cellphonewriter",
            name="input",
            field=models.TextField(
                help_text='\nSiga rigorosamente este formato: <br>\n<br>\nCORRIGIR:\n\n<br>\nMarca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>\nMarca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>\n\n<br>\n\nADICIONAR:\n\n<br>\nMarca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>\nMarca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3<br>\n\n<br>\n\nREMOVER:\n\n<br>\nMarca Modelo<br>\nMarca Modelo<br>\n\n<br>\n\n<hr class="solid">\n\nOpcionalmente, você pode colocar no final de cada linha de ação, uma data que queira que seja publicada aquele celular, Exemplo: <br>\n\n<br>\n\nMarca Modelo: Marca Modelo 1 - Marca Modelo 2 - Marca Modelo 3 [dd/mm/YYYY]<br>\n            ',
                verbose_name="Entrada",
            ),
        ),
    ]
