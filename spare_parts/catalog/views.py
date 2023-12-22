from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCard, Photo, Brand
from django.views.generic import ListView, DetailView


class SparesListView(ListView):
    model = ProductCard
    context_object_name = 'spares'
    paginate_by = 3
    
    
class SpareDetailView(DetailView):
    model = ProductCard
    context_object_name = 'spares'


def index(request):
    text_head = 'Каталог доступных запчастей'
    spares = ProductCard.objects.all()
    num_spares = ProductCard.objects.all().count()
    brand = Brand.objects
    num_brand = Brand.objects.count()
    photo = Photo.objects.all()

    context = {'text_head': text_head, 
               'spares': spares, 
               'num_spares': num_spares,
               'brand': brand,
               'num_brand': num_brand,
               'photo': photo}
    
    return render(request, 'catalog/index.html', context) 
