# Generated by Django 4.0.4 on 2022-05-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='dni',
            field=models.CharField(default=True, max_length=40),
        ),
    ]