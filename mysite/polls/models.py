from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Sale(models.Model):
    prod_desc = models.CharField(max_length=200)
    cost = models.FloatField(default=0.0)
    date_of_pur = models.DateTimeField('date published')
    def __str__(self):
        return self.prod_desc
    def was_published_recently(self):
        return self.date_of_pur >= timezone.now()-datetime.timedelta(days=1) 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)





