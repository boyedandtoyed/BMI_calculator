<<<<<<< HEAD
# Generated by Django 3.2 on 2021-04-13 02:34

from django.db import migrations, models
=======
# Generated by Django 3.2 on 2021-04-18 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> e3fe231 (height bug correction)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> e3fe231 (height bug correction)
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField(max_length=3)),
=======
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
>>>>>>> e3fe231 (height bug correction)
            ],
        ),
    ]
