# Generated by Django 4.0.6 on 2023-06-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_remove_portfolio_like_portfolio_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name_work_skill',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
