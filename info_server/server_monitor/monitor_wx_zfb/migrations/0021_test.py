# Generated by Django 2.1.5 on 2019-11-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_wx_zfb', '0020_auto_20191010_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsvd1', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
