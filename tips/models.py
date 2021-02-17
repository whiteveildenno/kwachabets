from django.db import models

from datetime import  datetime

# Create your models here.

class Tip(models.Model):
  country_name = models.CharField(max_length= 200)
  competition_name = models.CharField(max_length= 200)
  home_team = models.CharField(max_length= 200)
  away_team= models.CharField(max_length= 200)
  kick_off_time = models.TimeField(default= datetime.now)
  date_of_match = models.DateField(default = datetime.now)
  prediction = models.CharField(max_length= 200)  
  match_odds = models.DecimalField(max_digits= 5, decimal_places= 2, default = 1.00 )
  betslip_link = models.URLField(max_length=200, blank=True)
  bookmaker = models.CharField(max_length = 200)
  logo = models.ImageField(upload_to =  'photos/%Y/%m/%d/')
  image_seo = models.CharField(max_length = 200)
  is_published = models.BooleanField(default=True)
  def __str__(self):
    return self.competition_name
