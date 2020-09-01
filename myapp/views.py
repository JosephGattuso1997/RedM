from django.shortcuts import render, get_object_or_404

from myapp.models import Portfolio
# Create your views here.
def index(request):
    portfolioItems =  Portfolio.objects.all()
    context = {'items': portfolioItems}
    return render(request, 'index.html', context)


def details(request,slug):
    unique_slug = get_object_or_404(Portfolio, slug=slug)
    context= {'details': unique_slug,
              }
    return render(request, 'portfolio-details.html',context)


