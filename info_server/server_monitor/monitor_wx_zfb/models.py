from django.db import models

# Create your models here.
# 服务器配置表
class trans_flow(models.Model):
    #date = models.DateField()
    settle_date = models.CharField(max_length=12, blank=True,null=True,db_index=True) #日期
    txn_time = models.DateTimeField(db_index=True) #交易时间


    plat_area = models.CharField(max_length=64)    #平台区域
    plat_bu = models.CharField(max_length=64)       #BU部门
    plat_team = models.CharField(max_length=64)     #team团队
    plat_name = models.CharField(max_length=64,db_index=True)    #平台名称

    bank_id = models.CharField(max_length=64)
    bank_ch_name = models.CharField(max_length=128)

    trans_type = models.CharField(max_length=64)
    trans_chnl = models.CharField(max_length=64)

    trans_count_all = models.CharField(max_length=64, blank=True,null=True)
    trans_count_err = models.CharField(max_length=64, blank=True,null=True)
    trans_amt_all = models.CharField(max_length=64, blank=True,null=True)
    trans_amt_err = models.CharField(max_length=64, blank=True,null=True)

    trans_avg_time =  models.CharField(max_length=64, blank=True,null=True)
    rsvd1 =  models.CharField(max_length=64, blank=True,null=True)
    rsvd2 = models.CharField(max_length=64, blank=True, null=True)
    rsvd3 = models.CharField(max_length=64, blank=True, null=True)
    rsvd4 = models.CharField(max_length=64, blank=True, null=True)
    rsvd5 = models.CharField(max_length=64, blank=True, null=True)
    class Meta:
        unique_together = (("txn_time", "plat_area", "plat_bu", "plat_team", "plat_name", "bank_id", "bank_ch_name", "trans_type", "trans_chnl"),)

    def __str__(self):
        return "%s-%s-%s-%s-%s-%s" % (self.txn_time, self.plat_name, self.bank_ch_name,self.trans_type,self.trans_count_all,self.trans_count_err)

# class test(models.Model):
#     rsvd1 = models.CharField(max_length=64, blank=True, null=True)