# Generated by Django 3.2.15 on 2022-10-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0007_ipfs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipfs',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
