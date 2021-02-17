from django.contrib import admin
from  .models import Tip
# Register your models here.
class TipAdmin(admin.ModelAdmin):
  list_display = ('kick_off_time', 'competition_name', 'home_team', 'away_team', 'prediction', 'match_odds','is_published')
  list_display_links = ('kick_off_time', 'competition_name')
  list_filter = ('competition_name','kick_off_time',)
  list_editable = ('is_published',)
  search_fields = ('competition_name', 'home_team', 'away_team')
  list_per_page = 25

admin.site.register(Tip, TipAdmin)