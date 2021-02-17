from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from tips.models import Tip
from affiliates.models import Affiliate



# Create your views here.
def index(request):
  tips = Tip.objects.order_by('-date_of_match').filter(is_published=True)

  paginator = Paginator(tips, 12)
  page = request.GET.get('page')
  paged_tips = paginator.get_page(page)

  affiliates = Affiliate.objects.all().filter(is_published=True)

  context = {
    'tips': paged_tips,
    'affiliates': affiliates
  }

  return render(request, 'pages/index.html', context)

def privacy(request):
  return render(request, 'pages/privacy.html')

def terms(request):
  return render(request, 'pages/terms.html')


    
