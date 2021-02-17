from django.db import models

# Create your models here.

class Bookmaker(models.Model):
  bookmaker = models.CharField(max_length = 200)
  logo = models.ImageField(upload_to =  'photos/%Y/%m/%d/')
  image_seo = models.CharField(max_length = 200)
  review_title = models.CharField(max_length = 200)
  review_description = models.TextField()
  bonus_link = models.URLField(max_length=200, blank=True)
  is_published = models.BooleanField(default=True)
  def __str__(self):
      return self.bookmaker
