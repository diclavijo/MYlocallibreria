# Generated by Django 3.1.2 on 2020-11-13 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20201109_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alimentoinstance',
            options={'ordering': ['alimento']},
        ),
        migrations.RemoveField(
            model_name='alimentoinstance',
            name='alimen_dispo',
        ),
    ]