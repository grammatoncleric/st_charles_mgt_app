from django.db import models
from datetime import datetime

class Member(models.Model):
    user_id = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    resident_address = models.TextField(blank=True)
    office_address = models.TextField(blank=True)
    mobile_no = models.CharField(max_length=50)
    lga_origin = models.CharField(max_length=50)
    state_origin = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    married_in_catholic = models.BooleanField(default=False)
    nok_name = models.CharField(max_length=200)
    nok_phone = models.CharField(max_length=50)
    sacraments_received = models.TextField(blank=True)
    when_you_start_worship = models.CharField(max_length=50)
    belong_to_association = models.BooleanField(default=False)
    association_names = models.TextField(blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name