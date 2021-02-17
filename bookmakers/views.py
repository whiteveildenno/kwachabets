from django.shortcuts import render
from bookmakers.models import Bookmaker
from affiliates.models import Affiliate

# Create your views here.
def bookie(request):
  bookmakers = Bookmaker.objects.all().filter(is_published=True)
  affiliates = Affiliate.objects.all().filter(is_published=True)

  context = {
    'bookmakers': bookmakers,
    'affiliates': affiliates
  }

  return render(request, 'bookmakers/bookie.html', context)