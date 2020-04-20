from django.db import models

# Create your models here.
# 服务器配置表
class config(models.Model):
    #date = models.DateField()
    plat_id = models.CharField(max_length=128, blank=True,null=True)
    plat_name = models.CharField(max_length=128)
    name_ch = models.CharField(max_length=128)
    name = models.CharField(max_length=32, blank=True,null=True)
    user = models.CharField(max_length=64, blank=True,null=True)
    sys = models.CharField(max_length=64)
    ip = models.CharField(max_length=32)
    passwd = models.CharField(max_length=64, blank=True,null=True)
    #team 银行
    team = models.CharField(max_length=128, blank=True,null=True)
    worker = models.CharField(max_length=64, blank=True,null=True)
    bank = models.CharField(max_length=64, blank=True,null=True)
    port = models.CharField(max_length=64)
    ver = models.CharField(max_length=128, blank=True,null=True)
    objects = models.Manager()

    class Meta:
        unique_together = (("plat_id", "name"),)


    # def __str__(self):
    #     return "%s-%s-%s" % (self.plat_id, self.name, self.name_ch)

# 租户配置表
class config_discovery(models.Model):
    #date = models.DateField()
    plat = models.CharField(max_length=32)
    bank_id = models.CharField(max_length=32)
    bank_no = models.CharField(max_length=32)
    bank_name = models.CharField(max_length=128, blank=True,null=True)
    bank_group = models.CharField(max_length=32)
    objects = models.Manager()
    class Meta:
        unique_together = (("plat","bank_id","bank_no"),)
#     class Meta:
#         unique_together = (("plat"),("bank_id"),("bank_no"),)
# class config_discovery2(models.Model):
#     #date = models.DateField()
#     plat = models.CharField(max_length=32)
#     bank_id = models.CharField(max_length=32)
#     bank_no = models.CharField(max_length=32)
#     bank_name = models.CharField(max_length=128, blank=True,null=True)
#     bank_group = models.CharField(max_length=32)

#------------------------------V2.0 关系数据库设计---------------------------------------
# 一对一 OneToOneField         一条记录中只能选择一次，选择后其它记录不能再次选择
# 一对多 ForeignKey            一条记录中只能选择一次，可以被多次选择
# 多对多 ManyToManyField       一条记录中可以选择多次

# blank=True,null=True,default='1'
# 1、blank用于表单的认证，被设为blank=False（默认为False）的字段在填写表单时不能为空。
# 2、null用于规定数据库中的列的非空性，被设为null=False（默认为False）的字段在数据库中对应的列不能为空
# （用SQL来说明就是为该列添加了NOT NULL的约束)。
# 3、default 为默认值


# 服务器配置表
# class c_config(models.Model):
#     # 产品 ID 关联
#     plat = models.ForeignKey("i_plat", on_delete=models.CASCADE, )
#     #系统信息 ID 关联
#     app_server = models.ForeignKey("i_app_server", on_delete=models.CASCADE, blank=True,null=True)
#     # 银行 ID 关联
#     # bank = models.ManyToManyField("i_bank")
#     bank = models.ForeignKey("i_bank", on_delete=models.CASCADE, blank=True,null=True)
#     app_type = models.ForeignKey("i_app_type", on_delete=models.CASCADE, blank=True, null=True)
#     app_stat = models.ForeignKey("i_app_stat", on_delete=models.CASCADE, blank=True,null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     objects = models.Manager()
#
#     # bank = models.CharField(max_length=64, blank=True,null=True)
#
#
#     class Meta:
#         unique_together = (("plat", "app_server","bank"),)
#
#     def __str__(self):
#         return "%s %s" % (self.plat, self.app_server)

    # def bank_list(self):
    #     return ','.join([i.Name for i in self.bank.all()])

class c_config2(models.Model):
    # 产品 ID 关联
    plat = models.ForeignKey("i_plat", on_delete=models.CASCADE, )
    #系统信息 ID 关联
    app_server = models.ForeignKey("i_app_server", on_delete=models.CASCADE, blank=True,null=True)
    # 银行 ID 关联
    # bank = models.ManyToManyField("i_bank")
    app_bank = models.ForeignKey("i_bank", on_delete=models.CASCADE, blank=True,null=True)
    app_type = models.ForeignKey("i_app_type", on_delete=models.CASCADE, blank=True, null=True)
    app_stat = models.ForeignKey("i_app_stat", on_delete=models.CASCADE, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

class c_config_v1(models.Model):
    # 产品 ID 关联
    plat = models.ForeignKey("i_plat", on_delete=models.CASCADE, )
    #系统信息 ID 关联
    app_server = models.ForeignKey("i_app_server", on_delete=models.CASCADE, blank=True,null=True)
    # 银行 ID 关联
    app_bank = models.ManyToManyField("i_bank", blank=True)
    # bank = models.ForeignKey("i_bank", on_delete=models.CASCADE, blank=True,null=True)
    app_type = models.ForeignKey("i_app_type", on_delete=models.CASCADE, blank=True, null=True)
    app_stat = models.ForeignKey("i_app_stat", on_delete=models.CASCADE, blank=True,null=True)
    app_mode = models.ForeignKey("i_app_mode", on_delete=models.CASCADE, blank=True,null=True)


    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

# 产品表
class i_plat(models.Model):
    plat_id = models.CharField(max_length=128)
    # plat_ver = models.CharField(max_length=128, blank=True,null=True)
    plat_ver = models.ForeignKey("i_plat_ver", on_delete=models.CASCADE, blank=True, null=True)
    plat_name = models.CharField(max_length=128)
    plat_name_foreign = models.CharField(max_length=128, blank=True,null=True)
    plat_team = models.ForeignKey("i_app_team", on_delete=models.CASCADE, blank=True, null=True)

    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    class Meta:
        unique_together = (("plat_id", "plat_ver","plat_name"),)

    def __str__(self):
        return "%s_%s_%s" % (self.plat_ver, self.plat_id, self.plat_name)

# 产品版本
class i_plat_ver(models.Model):
    name = models.CharField(max_length=128, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return "%s" % (self.name)

#
class i_bank(models.Model):
    yhdm = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    name_ch = models.CharField(max_length=128)
    name_ch_foreign = models.CharField(max_length=128, blank=True,null=True)
    initiate_bank = models.ForeignKey("i_initiate_bank", on_delete=models.CASCADE, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    class Meta:
        unique_together = (("name"),("yhdm"),)


    def __str__(self):
        return "%s_%s" % (self.name, self.name_ch)

class i_initiate_bank(models.Model):
    name = models.CharField(max_length=32, blank=True,null=True)
    name_ch = models.CharField(max_length=128, blank=True,null=True)
    name_ch_foreign = models.CharField(max_length=128, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return "%s_%s" % (self.name, self.name_ch)


class i_app_server(models.Model):
    user = models.CharField(max_length=64, blank=True,null=True)
    # agent 版本关联
    agent_ver = models.ForeignKey("i_agent_ver", on_delete=models.CASCADE, blank=True,null=True)
    # 应用版本关联
    app_ver = models.CharField(max_length=64, blank=False,null=False, default='default')
    # app_ver = models.OneToOneField("i_app_ver", on_delete=models.CASCADE, blank=True,null=True)
    ip = models.CharField(max_length=32)
    passwd = models.CharField(max_length=64, blank=True,null=True)
    port = models.CharField(max_length=64)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    class Meta:
        unique_together = (("ip"),("port"),)

    # ver = models.CharField(max_length=128, blank=True,null=True)
    def __str__(self):
        return "%s_%s" % (self.user, self.ip)

class i_agent_ver(models.Model):
    name = models.CharField(max_length=64, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return "%s" % (self.name)

class i_app_type(models.Model):
    type_id = models.CharField(max_length=64, blank=True,null=True)
    type_name = models.CharField(max_length=64, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return "%s_%s" % (self.type_id, self.type_name)

class i_app_stat(models.Model):
    stat_id = models.IntegerField(null=True)
    stat_name = models.CharField(max_length=64, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return "%s_%s" % (self.stat_id, self.stat_name)

class i_app_mode(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=128)
    objects = models.Manager()
    def __str__(self):
        return "%s_%s" % (self.code, self.name)

class i_app_team(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=128)
    objects = models.Manager()
    def __str__(self):
        return "%s_%s" % (self.code, self.name)


class user_info(models.Model):
    first_name = models.CharField(max_length=128, unique=True)
    qq_no = models.CharField(max_length=128, blank=True,null=True)
    group = models.ForeignKey("i_user_group", on_delete=models.PROTECT, blank=True,null=True)
    score = models.IntegerField(default=0)

class i_user_group(models.Model):
    code = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return "%s_%s" % (self.code, self.name)

# 用户操作表
class action(models.Model):
    app_type = models.ForeignKey("action_app_type", on_delete=models.CASCADE)
    action_type = models.ForeignKey("action_type", on_delete=models.CASCADE)
    info_id = models.IntegerField(default=0)
    text = models.CharField(max_length=256)
    oper = models.CharField(max_length=32)
    date = models.DateTimeField()
    score = models.IntegerField(default=0)

class action_app_type(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    def __str__(self):
        return "%s_%s" % (self.code, self.name)

# 操作类型 -- 查询、更新、追加
class action_type(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    # 操作分值
    score = models.IntegerField(default=0)
    def __str__(self):
        return "%s_%s" % (self.code, self.name)







