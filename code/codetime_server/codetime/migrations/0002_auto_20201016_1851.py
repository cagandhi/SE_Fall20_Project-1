# Generated by Django 3.1 on 2020-10-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codetime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='api_token',
            field=models.CharField(max_length=200),
        ),
    ]
