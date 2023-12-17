from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCard, Photo, Brand


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
