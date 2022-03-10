# Generated by Django 4.0.2 on 2022-03-09 21:59

from django.db import migrations, models
import django.utils.timezone
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_id', s3direct.fields.S3DirectField(blank=True)),
                ('pic_upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
