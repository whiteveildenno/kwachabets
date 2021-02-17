from django.contrib import admin
from  .models import Bookmaker
# Register your models here.
class BookmakerAdmin(admin.ModelAdmin):
  list_display = ('bookmaker', 'review_title','is_published')
  list_display_links = ('bookmaker',)
  list_editable = ('is_published',)
  search_fields = ('bookmaker',)
  list_per_page = 25
admin.site.register(Bookmaker, BookmakerAdmin)
