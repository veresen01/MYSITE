# Generated by Django 5.0.2 on 2024-03-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_master_alter_vitrazh_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='biography',
            field=models.TextField(verbose_name='О себе'),
        ),
    ]
