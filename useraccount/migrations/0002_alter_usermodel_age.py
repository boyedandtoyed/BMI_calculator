# Generated by Django 3.2 on 2021-04-13 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.IntegerField(),
        ),
    ]
