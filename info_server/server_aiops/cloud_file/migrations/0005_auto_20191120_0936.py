# Generated by Django 2.1.5 on 2019-11-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_file', '0004_info_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='file_path',
            field=models.CharField(max_length=64),
        ),
    ]
