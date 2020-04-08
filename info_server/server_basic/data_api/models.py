from django.db import models

# Create your models here.
class api(models.Model):
    api_id = models.IntegerField(null=True)
    url = models.CharField(max_length=128,unique=True)
    text = models.CharField(max_length=250,unique=True)
    par = models.CharField(max_length=128,null=True)
    dev_oper = models.CharField(max_length=10,null=True)

    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (("url"),("api_id"),)

    def __str__(self):
        return "%s %s %s" % (self.api_id, self.url, self.text)