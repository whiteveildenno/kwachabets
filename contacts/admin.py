from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('company_name', 'email_address', 'contact_date')
  list_display_links = ("company_name", "email_address")
  search_fields = ("company_name", "email_address")
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
