# Generated by Django 4.0.6 on 2023-04-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contectMe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contectme',
            name='emailC',
            field=models.EmailField(max_length=300),
        ),
    ]