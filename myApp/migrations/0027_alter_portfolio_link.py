# Generated by Django 4.1.3 on 2024-05-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0026_portfolio_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
