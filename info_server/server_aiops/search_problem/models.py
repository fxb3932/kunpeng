from django.db import models

# Create your models here.
class info(models.Model):
    # date = models.DateField()
    # date = models.DateTimeField()
    title = models.CharField(max_length=250,unique=True)
    trans_code = models.CharField(max_length=64, blank=True)
    trans_err = models.CharField(max_length=512, blank=True)
    problem_info = models.CharField(max_length=3000, blank=True)
    problem_answer = models.CharField(max_length=4500,blank=True)
    problem_answer_txt = models.CharField(max_length=4500,blank=True)


    bank_id = models.CharField(max_length=32, null=True, blank=True)
    bank_oper = models.CharField(max_length=32, null=True, blank=True)
    problem_source = models.CharField(max_length=32, null=True, blank=True)

    # 问题制作时间、下发完成时间、操作人
    input_date = models.DateTimeField(null=True, blank=True)
    answer_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)


    # 录入
    input_oper = models.CharField(max_length=64, null=True, blank=True)
    # 指派
    assign_oper = models.CharField(max_length=64, null=True, blank=True)
    # 解答
    answer_oper = models.CharField(max_length=64, null=True, blank=True)
    # 更新
    update_oper = models.CharField(max_length=64, null=True, blank=True)

    #20200108 工单号，版本制作复核人
    update_chk_oper = models.CharField(max_length=64, null=True, blank=True)

    # 0-已录入未解答 1-已解答 2-问题退回审核中 3-新解答审核中
    # stat = models.IntegerField(blank=True, null=True)
    t_stat = models.ForeignKey("info_stat", on_delete=models.PROTECT, blank=True, null=True)
    t_channel = models.ForeignKey("info_channel", on_delete=models.PROTECT, blank=True, null=True)
    t_type = models.ForeignKey("info_type", on_delete=models.PROTECT, blank=True, null=True)

    # 1-知识库认证
    info_check_flag = models.IntegerField()
    # 1-有新评论标准答案待更新
    info_check_update = models.IntegerField()


    # 查询次数
    count_search = models.IntegerField(null=True)

    # 点击次数
    count_chick = models.IntegerField(null=True)

    # 评论
    comments_update_date = models.DateTimeField(null=True, blank=True)
    t_comments = models.ManyToManyField("info_comments", blank=True)


class info_stat(models.Model):
    stat_id = models.IntegerField(null=True, db_index = True)
    stat_name = models.CharField(max_length=64, blank=True,null=True)
    def __str__(self):
        return "%s_%s" % (self.stat_id, self.stat_name)

class info_channel(models.Model):
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=64, blank=True,null=True)
    def __str__(self):
        return "%s_%s" % (self.code, self.name)

class info_type(models.Model):
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=64, blank=True,null=True)
    def __str__(self):
        return "%s_%s" % (self.code, self.name)

class info_comments(models.Model):
    # code = models.IntegerField(null=True)
    name = models.CharField(max_length=2048)
    update_oper = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    i_stat = models.ForeignKey("info_comments_stat", on_delete=models.CASCADE, blank=True,null=True)

    # class Meta:
    #     unique_together = (("name", "update_oper", 'update_date'),)

    def __str__(self):
        return "%s_%s" % (self.name, self.update_oper)

class info_comments_stat(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=64)
    def __str__(self):
        return "%s_%s" % (self.code, self.name)

class action(models.Model):
    type = models.ForeignKey("action_type", on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    oper = models.CharField(max_length=32)
    date = models.DateTimeField()

# 操作类型 -- 查询、更新、追加
class action_type(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=64)
    score = models.IntegerField(default=0)
    def __str__(self):
        return "%s_%s" % (self.code, self.name)
