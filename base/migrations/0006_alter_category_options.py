# Generated by Django 4.1.7 on 2023-06-19 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
