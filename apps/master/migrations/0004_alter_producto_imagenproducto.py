# Generated by Django 4.2.2 on 2023-07-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_producto_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(max_length=200, upload_to='productos'),
        ),
    ]