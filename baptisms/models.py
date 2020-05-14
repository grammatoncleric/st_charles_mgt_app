from django.db import models
from datetime import datetime

class Baptism(models.Model):
        user_id = models.IntegerField(blank=True)
        bap_first_name = models.CharField(max_length=50)
        bap_middle_name = models.CharField(max_length=50)
        bap_last_name = models.CharField(max_length=50)
        date_of_birth = models.CharField(max_length=50)
        place_of_birth = models.CharField(max_length=50)
        home_town = models.CharField(max_length=50)
        state_origin = models.CharField(max_length=50)
        adult_mobile_no = models.CharField(max_length=50)
        fathers_name = models.CharField(max_length=50)
        fathers_mobile_no = models.CharField(max_length=50)
        mothers_name = models.CharField(max_length=50)
        mothers_mobile_no = models.CharField(max_length=50)
        parents_address =  models.TextField(blank=True)
        parents_marital_status = models.CharField(max_length=50)
        parents_marriage_parish = models.CharField(max_length=200)
        god_fathers_name = models.CharField(max_length=50)
        god_fathers_mobile_no = models.CharField(max_length=50)
        god_fathers_address =  models.TextField(blank=True)
        god_mothers_name = models.CharField(max_length=50)
        god_mothers_mobile_no = models.CharField(max_length=50)
        god_mothers_address = models.TextField(blank=True)
        digital_signature = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
        create_date = models.DateTimeField(default=datetime.now, blank=True)

        def __str__(self):
           return self.bap_first_name