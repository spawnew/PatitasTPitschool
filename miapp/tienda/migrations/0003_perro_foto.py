# Generated by Django 5.1.4 on 2025-01-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_rename_buscarperro_perro'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='./static/css/fotos/siber.jpg'),
        ),
    ]