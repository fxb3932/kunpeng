# Generated by Django 2.1.5 on 2020-04-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans_zl_helloworld', '0005_auto_20200402_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yything',
            name='reason',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='title',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
