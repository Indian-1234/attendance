# Generated by Django 4.2 on 2023-04-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_attendance_afternoon_attendance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.TextField()),
                ('dep', models.TextField()),
                ('data', models.TextField()),
                ('fnattnd', models.BooleanField()),
                ('anattnd', models.BooleanField()),
            ],
        ),
    ]