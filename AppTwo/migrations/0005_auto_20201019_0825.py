# Generated by Django 3.1.1 on 2020-10-19 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0004_auto_20201019_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='expiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]