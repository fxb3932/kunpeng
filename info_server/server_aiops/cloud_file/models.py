from django.db import models

# Create your models here.
class info(models.Model):
    # 文件名
    file_name = models.CharField(max_length=64)
    # 大小
    file_size = models.CharField(max_length=64)
    # 更新人
    update_oper = models.CharField(max_length=64)
    # 更新时间
    update_date = models.DateTimeField()
    # 对象类型
    file_type = models.CharField(max_length=64)
    # 所属目录
    file_path = models.CharField(max_length=64)
    # 描述
    # 标签
    # 评论
    # 历史版本
    # 操作记录
    # 下载记录

    class Meta:
        unique_together = (("file_name", "file_path"),)
