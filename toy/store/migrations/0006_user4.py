# Generated by Django 5.1.6 on 2025-02-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_name_user3_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='user4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user4',
            },
        ),
    ]
