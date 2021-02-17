from django.contrib import admin
from  .models import Affiliate
# Register your models here.
class AffiliateAdmin(admin.ModelAdmin):
  list_display = ('company_name','is_published')
  list_display_links = ('company_name',)
  list_editable = ('is_published',)
  search_fields = ('company_name',)
  list_per_page = 12
admin.site.register(Affiliate, AffiliateAdmin)
