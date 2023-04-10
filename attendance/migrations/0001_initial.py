# Generated by Django 4.1.7 on 2023-04-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('name', models.TextField()),
                ('logo', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffName', models.TextField()),
                ('staffDep', models.TextField()),
                ('staffCollege', models.TextField()),
                ('staffPosition', models.TextField()),
                ('staffUsername', models.TextField()),
                ('staffPassword', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('reg', models.TextField()),
                ('s_mobile', models.TextField()),
                ('p_mobile', models.TextField()),
                ('attendance', models.BooleanField(default=False)),
                ('clg', models.TextField()),
                ('department', models.TextField()),
                ('year', models.TextField()),
                ('date_field', models.DateField(null=True)),
            ],
        ),
    ]
