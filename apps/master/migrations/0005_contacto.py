# Generated by Django 4.2.2 on 2023-07-11 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_alter_producto_imagenproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('telefono', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
            ],
        ),
    ]
