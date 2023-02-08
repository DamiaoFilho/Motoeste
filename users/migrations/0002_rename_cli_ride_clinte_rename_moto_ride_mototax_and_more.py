# Generated by Django 4.1.6 on 2023-02-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='cli',
            new_name='clinte',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='moto',
            new_name='motoTax',
        ),
        migrations.AddField(
            model_name='ride',
            name='end',
            field=models.CharField(default=None, max_length=300, verbose_name='Chegada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='start',
            field=models.CharField(default=None, max_length=300, verbose_name='Começo'),
            preserve_default=False,
        ),
    ]
