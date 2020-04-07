from django.db import models

# Create your models here.
class info(models.Model):
    group = models.CharField(max_length=128)
    date = models.DateTimeField()
    oper = models.CharField(max_length=128)
    content = models.CharField(max_length=2048)

    class Meta:
        unique_together = (("group", "date", 'oper'),)