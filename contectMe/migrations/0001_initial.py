# Generated by Django 4.0.6 on 2023-04-01 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContectMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=30)),
                ('emailC', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.TextField()),
            ],
        ),
    ]
