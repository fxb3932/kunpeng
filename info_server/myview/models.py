from django.db import models

# Create your models here.
#时间
#用户
#页面ID
#页面title
#浏览器
#访问类型
class Article(models.Model):
    #date = models.DateField()
    date = models.DateTimeField()
    user = models.CharField(max_length=30)
    html_id = models.CharField(max_length=30)
    html_title = models.CharField(max_length=128)
    browser_name = models.CharField(max_length=64)
    connect_type = models.CharField(max_length=64)

    def __str__(self):
        return "%s-%s-%s" % (self.date, self.user, self.html_id)
