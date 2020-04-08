# Generated by Django 2.1.5 on 2020-03-12 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='c_config2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_config_v1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_id', models.CharField(blank=True, max_length=128, null=True)),
                ('plat_name', models.CharField(max_length=128)),
                ('name_ch', models.CharField(max_length=128)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('user', models.CharField(blank=True, max_length=64, null=True)),
                ('sys', models.CharField(max_length=64)),
                ('ip', models.CharField(max_length=32)),
                ('passwd', models.CharField(blank=True, max_length=64, null=True)),
                ('team', models.CharField(blank=True, max_length=128, null=True)),
                ('worker', models.CharField(blank=True, max_length=64, null=True)),
                ('bank', models.CharField(blank=True, max_length=64, null=True)),
                ('port', models.CharField(max_length=64)),
                ('ver', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='config_discovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat', models.CharField(max_length=32)),
                ('bank_id', models.CharField(max_length=32)),
                ('bank_no', models.CharField(max_length=32)),
                ('bank_name', models.CharField(blank=True, max_length=128, null=True)),
                ('bank_group', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='i_agent_ver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='i_app_mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='i_app_server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=64, null=True)),
                ('app_ver', models.CharField(default='default', max_length=64)),
                ('ip', models.CharField(max_length=32)),
                ('passwd', models.CharField(blank=True, max_length=64, null=True)),
                ('port', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('agent_ver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_agent_ver')),
            ],
        ),
        migrations.CreateModel(
            name='i_app_stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_id', models.IntegerField(null=True)),
                ('stat_name', models.CharField(blank=True, max_length=64, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='i_app_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='i_app_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.CharField(blank=True, max_length=64, null=True)),
                ('type_name', models.CharField(blank=True, max_length=64, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='i_bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yhdm', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('name_ch', models.CharField(max_length=128)),
                ('name_ch_foreign', models.CharField(blank=True, max_length=128, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='i_initiate_bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('name_ch', models.CharField(blank=True, max_length=128, null=True)),
                ('name_ch_foreign', models.CharField(blank=True, max_length=128, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='i_plat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_id', models.CharField(max_length=128)),
                ('plat_name', models.CharField(max_length=128)),
                ('plat_name_foreign', models.CharField(blank=True, max_length=128, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('plat_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_team')),
            ],
        ),
        migrations.CreateModel(
            name='i_plat_ver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='i_plat',
            name='plat_ver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_plat_ver'),
        ),
        migrations.AddField(
            model_name='i_bank',
            name='initiate_bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_initiate_bank'),
        ),
        migrations.AlterUniqueTogether(
            name='config_discovery',
            unique_together={('plat', 'bank_id', 'bank_no')},
        ),
        migrations.AlterUniqueTogether(
            name='config',
            unique_together={('plat_id', 'name')},
        ),
        migrations.AddField(
            model_name='c_config_v1',
            name='app_bank',
            field=models.ManyToManyField(to='cmdb.i_bank'),
        ),
        migrations.AddField(
            model_name='c_config_v1',
            name='app_mode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_mode'),
        ),
        migrations.AddField(
            model_name='c_config_v1',
            name='app_server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_server'),
        ),
        migrations.AddField(
            model_name='c_config_v1',
            name='app_stat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_stat'),
        ),
        migrations.AddField(
            model_name='c_config_v1',
            name='app_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_type'),
        ),
        migrations.AddField(
            model_name='c_config_v1',
            name='plat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_plat'),
        ),
        migrations.AddField(
            model_name='c_config2',
            name='app_bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_bank'),
        ),
        migrations.AddField(
            model_name='c_config2',
            name='app_server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_server'),
        ),
        migrations.AddField(
            model_name='c_config2',
            name='app_stat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_stat'),
        ),
        migrations.AddField(
            model_name='c_config2',
            name='app_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_app_type'),
        ),
        migrations.AddField(
            model_name='c_config2',
            name='plat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.i_plat'),
        ),
        migrations.AlterUniqueTogether(
            name='i_plat',
            unique_together={('plat_id', 'plat_ver', 'plat_name')},
        ),
        migrations.AlterUniqueTogether(
            name='i_bank',
            unique_together={('name', 'yhdm')},
        ),
        migrations.AlterUniqueTogether(
            name='i_app_server',
            unique_together={('ip', 'port')},
        ),
    ]