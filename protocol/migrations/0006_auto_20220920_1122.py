# Generated by Django 3.2.15 on 2022-09-20 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0005_auto_20220919_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='gas',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='gas_price',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='to_account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='value',
        ),
    ]
