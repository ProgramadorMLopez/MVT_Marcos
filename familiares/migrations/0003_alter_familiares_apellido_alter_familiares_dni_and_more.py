# Generated by Django 4.0.4 on 2022-05-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0002_alter_familiares_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='apellido',
            field=models.CharField(default=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='familiares',
            name='dni',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='familiares',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
