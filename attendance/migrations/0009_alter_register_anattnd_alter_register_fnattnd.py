# Generated by Django 4.2 on 2023-04-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_register_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='anattnd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='fnattnd',
            field=models.BooleanField(default=False),
        ),
    ]