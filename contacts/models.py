from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
  company_name = models.CharField(max_length= 200)
  email_address = models.CharField(max_length=100)
  messager = models.TextField(blank=True)
  contact_date = models.DateField(default = datetime.now, blank = True)
  def __str__(self):
    return self.company_name