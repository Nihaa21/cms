# Generated by Django 3.1.1 on 2020-11-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0013_client_time_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sll_expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='time_spent',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
