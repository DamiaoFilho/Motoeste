# Generated by Django 4.1.6 on 2023-02-10 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='motoTax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Site.mototaxi', verbose_name='Moto Taxi'),
        ),
    ]
