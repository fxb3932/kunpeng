from django.db import models

# Create your models here.
class flow(models.Model):
    #date = models.DateField()
    date = models.DateTimeField()
    rjxf_id = models.CharField(max_length=64,unique=True)
    rjxf_type = models.CharField(max_length=4)
    rjxf_txt = models.CharField(max_length=512)
    file_name = models.CharField(max_length=256)
    file_size = models.CharField(max_length=64)
    rjxf_run_date = models.DateTimeField(blank=True,null=True)
    rjxf_stat = models.CharField(max_length=64, blank=True, null=True)
    chk_stat = models.CharField(max_length=64, blank=True, null=True)
    rjxf_num_count = models.IntegerField(null=True)

    #20191101 版本制作时间、下发完成时间、操作人
    make_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(null=True)
    make_oper = models.CharField(max_length=64, null=True)
    update_oper = models.CharField(max_length=64, null=True)

    #20200108 工单号，版本制作复核人
    itsm_no = models.CharField(max_length=64, null=True)
    make_chk_oper = models.CharField(max_length=64, null=True)


#合规目录表
class file_dir(models.Model):
    name = models.CharField(max_length=64,unique=True)
    name_ch = models.CharField(max_length=64, blank=True, null=True)

#163.1.6.10软件下发目录管理表
class ftp_path(models.Model):
    ftp_id = models.CharField(max_length=64,unique=True)
    ftp_pwd = models.CharField(max_length=64, unique=True)
