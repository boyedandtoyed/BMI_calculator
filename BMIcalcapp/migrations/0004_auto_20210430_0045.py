# Generated by Django 3.2 on 2021-04-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMIcalcapp', '0003_rename_suggestions_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='higher_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='lower_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]