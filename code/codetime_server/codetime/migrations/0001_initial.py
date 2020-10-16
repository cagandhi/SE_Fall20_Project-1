# Generated by Django 3.1 on 2020-10-16 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('log_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('api_token', models.CharField(default='5e260de3-9ed7-4604-a2cb-9e6ee210ca78gFAZEiIjcQ30lsGC', max_length=32)),
            ],
            options={
                'db_table': 'log_user',
            },
        ),
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('log_file_time_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=1000)),
                ('file_extension', models.CharField(blank=True, max_length=20, null=True)),
                ('detected_language', models.CharField(blank=True, max_length=50, null=True)),
                ('log_date', models.DateField()),
                ('log_timestamp', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('log_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='codetime.user')),
            ],
            options={
                'db_table': 'log_file_time',
            },
        ),
    ]
