# Generated by Django 2.1.5 on 2020-03-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_problem', '0004_auto_20200326_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='problem_answer',
            field=models.CharField(blank=True, max_length=4500),
        ),
        migrations.AlterField(
            model_name='info',
            name='problem_answer_txt',
            field=models.CharField(blank=True, max_length=4500),
        ),
    ]
