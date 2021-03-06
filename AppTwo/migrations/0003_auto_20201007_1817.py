# Generated by Django 3.1.1 on 2020-10-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0002_auto_20201007_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
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
        migrations.DeleteModel(
            name='clients',
        ),
    ]
