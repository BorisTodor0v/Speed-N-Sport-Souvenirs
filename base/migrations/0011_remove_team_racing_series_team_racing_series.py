# Generated by Django 4.1.7 on 2023-06-25 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_product_series_category_teams_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='racing_series',
        ),
        migrations.AddField(
            model_name='team',
            name='racing_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.racingseries'),
        ),
    ]
