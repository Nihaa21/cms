# Generated by Django 3.1.1 on 2020-11-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0014_auto_20201107_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sll_expiry_date',
            field=models.DateField(null=True),
        ),
    ]
