# Generated by Django 2.1.5 on 2019-11-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_file', '0003_auto_20191120_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='file_path',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
