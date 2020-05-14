from django.db import models
from datetime import datetime

class Enquiry(models.Model):
    user_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    enquiry_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
      return self.name