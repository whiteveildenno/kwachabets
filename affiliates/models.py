from django.db import models

# Create your models here.

class Affiliate(models.Model):
  company_name = models.CharField(max_length = 200)
  affiliate_link = models.URLField(max_length=200, blank=True)
  side_banner = models.ImageField(upload_to =  'photos/%Y/%m/%d/')
  main_banner = models.ImageField(upload_to =  'photos/%Y/%m/%d/')
  image_seo = models.CharField(max_length = 200)
  is_published = models.BooleanField(default=True)
  def __str__(self):
      return self.company_name