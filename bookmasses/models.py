from django.db import models
from datetime import datetime

class Bookmass(models.Model):
    user_id = models.IntegerField(blank=True)
    bookmass_time = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    fullname = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=50)
    names_to_pray_for = models.TextField(blank=True)
    intention = models.TextField(blank=True)
    intention_category = models.CharField(max_length=200)    
    intention_start_date = models.DateTimeField(default=datetime.now, blank=True)
    intention_end_date = models.DateTimeField(default=datetime.now, blank=True)
    amount_paid = models.CharField(max_length=50)
    have_open_thanksgiving = models.BooleanField(default=False)
    thanksgiving_day= models.CharField(max_length=50, blank=True)
    thanksgiving_time= models.CharField(max_length=50, blank=True)
    photo_pay_evidence = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.intention


    