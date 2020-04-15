from django.db import models


# Create your models here.
class yything(models.Model):
    title = models.CharField(max_length=2048, blank=True, null=False, default='')
    reason = models.CharField(max_length=2048, blank=True, null=False)
    banknames = models.CharField(max_length=128, blank=True, null=False)
    deal_person = models.CharField(max_length=64, blank=True, null=False)
    support_org = models.CharField(max_length=64, blank=True, null=False, default='')
    stat = models.CharField(max_length=16, blank=True, null=False, default='')
    diffcult = models.CharField(max_length=2048, blank=True, null=False, default='')
    beizhu = models.CharField(max_length=2048, blank=True, null=False, default='')  # 备注
    t_team = models.CharField(max_length=2048, blank=True, null=False, default='')  # 处理团队
    genjin = models.CharField(max_length=16, blank=True, null=False)  # 是否需继续跟进
    yanzheng = models.CharField(max_length=16, blank=True, null=False)  # 是否得到客户验证

    # 问题制作时间、下发完成时间、操作人
    want_date = models.DateTimeField(null=True, blank=True)  # 期望完成时间
    submit_person = models.CharField(max_length=64, blank=True, null=False)  # 报告人
    submit_date = models.DateTimeField(null=True, blank=True)  # 提出时间
    close_date = models.DateTimeField(null=True, blank=True)  # 实际完成时间
    t_stat = models.ForeignKey("yything_stat", on_delete=models.PROTECT, blank=True, null=True)  # 状态
    t_type = models.ForeignKey("enum_type", on_delete=models.PROTECT, blank=True, null=True)  # 类型
    t_zycd = models.ForeignKey("enum_zycd", on_delete=models.PROTECT, blank=True, null=True)  # 重要程度
    t_jjcd = models.ForeignKey("enum_jjcd", on_delete=models.PROTECT, blank=True, null=True)  # 紧急程度


class yything_stat(models.Model):
    stat_id = models.IntegerField(null=True)
    stat_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "%s_%s" % (self.stat_id, self.stat_name)


class enum_type(models.Model):
    type_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "type_name : %s" % (self.type_name)


class enum_zycd(models.Model):
    zycd_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "zycd_name : %s" % (self.zycd_name)


class enum_jjcd(models.Model):
    jjcd_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "jjcd_name : %s" % (self.jjcd_name)


class enum_team(models.Model):
    team_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "team_name : %s" % (self.team_name)


class enum_department(models.Model):
    department_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "department_name : %s" % (self.department_name)
