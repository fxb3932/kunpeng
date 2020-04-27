from django.db import models

# Create your models here.
class info(models.Model):
    group = models.CharField(max_length=128)
    date = models.DateTimeField()
    oper = models.CharField(max_length=128)
    content = models.CharField(max_length=2048)

    class Meta:
        unique_together = (("group", "date", 'oper'),)

class qq_data_count_bank_other(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % (self.name)

# list_bank_cz_count
class qq_data_count_bank_cz(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % (self.name)

# list_bank_big_count
class qq_data_count_bank_big(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % (self.name)