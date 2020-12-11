# Generated by Django 3.1.1 on 2020-10-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('reference', models.CharField(max_length=30)),
                ('project_name', models.CharField(max_length=30)),
                ('domain_name', models.CharField(max_length=30)),
                ('acc_name', models.CharField(max_length=30)),
                ('acc_password', models.CharField(max_length=30)),
                ('purchase_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
