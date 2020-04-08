from django.db import models


# Create your models here.
class chnltrans(models.Model):
    settle_date = models.DateField(db_index=True)
    bank_id = models.CharField(max_length=32)
    bank_name = models.CharField(max_length=128, db_index=True)
    zfjg_name = models.CharField(max_length=256, db_index=True)
    tran_tot = models.CharField(max_length=32)
    tran_tot_amt = models.CharField(max_length=64)

    class Meta:
        unique_together = (("settle_date", "bank_name", "zfjg_name"),)

    def __str__(self):
        return "%s-%s-%s-%s" % (self.settle_date, self.bank_name, self.zfjg_name, self.tran_tot)