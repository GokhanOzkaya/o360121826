# Generated by Django 4.0 on 2022-11-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('soyad', models.CharField(max_length=50)),
                ('açıklama', models.CharField(max_length=50)),
            ],
        ),
    ]
