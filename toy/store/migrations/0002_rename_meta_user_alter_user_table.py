# Generated by Django 5.1.6 on 2025-02-19 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meta',
            new_name='user',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
