# Generated by Django 3.2.9 on 2022-06-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_check_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
