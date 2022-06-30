# Generated by Django 3.2.9 on 2022-01-31 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20220129_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='hometask',
            name='id_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='school.type'),
        ),
    ]
