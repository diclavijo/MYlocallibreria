# Generated by Django 3.1.2 on 2020-11-07 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20201027_2012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
