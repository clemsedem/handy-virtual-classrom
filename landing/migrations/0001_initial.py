# Generated by Django 3.0.5 on 2020-04-17 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('class_id', models.CharField(max_length=9)),
                ('schedule_title', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False, verbose_name='open or closed status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'scheduled_classes',
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('extrid', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.ScheduleClass')),
            ],
            options={
                'db_table': 'class_rooms',
            },
        ),
    ]