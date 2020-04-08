# Generated by Django 2.1.5 on 2020-04-02 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trans_zl_helloworld', '0003_auto_20200402_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='enum_jjcd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jjcd_name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='enum_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='enum_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='enum_zycd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zycd_name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='yything',
            name='beizhu',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='yything',
            name='submit_person',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='banknames',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='deal_person',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='diffcult',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='reason',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='stat',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='support_org',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='yything',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='yything',
            name='t_jjcd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trans_zl_helloworld.enum_jjcd'),
        ),
        migrations.AddField(
            model_name='yything',
            name='t_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trans_zl_helloworld.enum_team'),
        ),
        migrations.AddField(
            model_name='yything',
            name='t_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trans_zl_helloworld.enum_type'),
        ),
        migrations.AddField(
            model_name='yything',
            name='t_zycd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trans_zl_helloworld.enum_zycd'),
        ),
    ]