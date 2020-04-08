# Generated by Django 2.1.5 on 2019-10-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monitor_wx_zfb', '0006_delete_trans_flow'),
    ]

    operations = [
        migrations.CreateModel(
            name='trans_flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settle_date', models.CharField(blank=True, db_index=True, max_length=12, null=True)),
                ('txn_time', models.DateTimeField(db_index=True)),
                ('plat_area', models.CharField(blank=True, default='AREA', max_length=64, null=True)),
                ('plat_bu', models.CharField(blank=True, default='BY', max_length=64, null=True)),
                ('plat_team', models.CharField(blank=True, default='TEAN', max_length=64, null=True)),
                ('plat_name', models.CharField(blank=True, db_index=True, max_length=64, null=True)),
                ('bank_id', models.CharField(blank=True, default='0', max_length=64, null=True)),
                ('bank_ch_name', models.CharField(blank=True, max_length=128, null=True)),
                ('trans_type', models.CharField(blank=True, max_length=64, null=True)),
                ('trans_chnl', models.CharField(blank=True, default='CHNL', max_length=64, null=True)),
                ('trans_count_all', models.CharField(blank=True, max_length=64, null=True)),
                ('trans_count_err', models.CharField(blank=True, max_length=64, null=True)),
                ('trans_amt_all', models.CharField(blank=True, max_length=64, null=True)),
                ('trans_amt_err', models.CharField(blank=True, max_length=64, null=True)),
                ('trans_avg_time', models.CharField(blank=True, max_length=64, null=True)),
                ('rsvd1', models.CharField(blank=True, max_length=64, null=True)),
                ('rsvd2', models.CharField(blank=True, max_length=64, null=True)),
                ('rsvd3', models.CharField(blank=True, max_length=64, null=True)),
                ('rsvd4', models.CharField(blank=True, max_length=64, null=True)),
                ('rsvd5', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='trans_flow',
            unique_together={('txn_time', 'plat_area', 'plat_bu', 'plat_team', 'plat_name', 'bank_id', 'bank_ch_name', 'trans_type', 'trans_chnl')},
        ),
    ]
