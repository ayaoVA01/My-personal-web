# Generated by Django 4.0.6 on 2023-06-12 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_alter_skill_name_work_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['sub_blog', '-explain_blog'], 'verbose_name_plural': 'Blog'},
        ),
    ]