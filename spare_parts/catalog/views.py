from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import AddSpareForm, PhotoFormSet
from .models import ProductCard, Photo, Brand, Category


class SparesListView(ListView):
    model = ProductCard
    context_object_name = 'spares'
    paginate_by = 3
    
    
class SpareDetailView(DetailView):
    model = ProductCard
    context_object_name = 'spares'
    
    
class BrandListView(ListView):
    model = Brand
    paginate_by = 5


def index(request):
    text_head = 'Каталог доступных запчастей'
    spares = ProductCard.objects.all()
    num_spares = ProductCard.objects.all().count()
    brand = Brand.objects
    num_brand = Brand.objects.count()
    photo = Photo.objects.all()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'text_head': text_head, 
               'spares': spares, 
               'num_spares': num_spares,
               'brand': brand,
               'num_brand': num_brand,
               'photo': photo,
               'num_visits': num_visits}
    
    return render(request, 'catalog/index.html', context) 


def about(request):
    text_head = 'Сведения о компании'
    name = 'Авторазбор г. Тольятти'
    used_spare_parts = ' Продажа б/у автозапчастей'
    used_tires = 'Продажа б/у шин'
    used_rims = 'Продажа б/у дисков'
    car_buyback = 'Выкуп автомобиля в любом состоянии'
    
    context = {
        'text_head': text_head,
        'name': name,
        'used_spare_parts': used_spare_parts,
        'used_tires': used_tires,
        'used_rims': used_rims,
        'car_buyback': car_buyback
    }
    
    return render(request, 'catalog/about.html', context)
   
   
def contact(request):
    text_head = 'Контакты'
    name = 'Авторазбор г. Тольятти'
    address = 'г. Тольятти, ул. Примерная, 123'
    phone = '+7 123 456 789'
    mail = 'avtorazbor@yandex.ru'
    
    context = {
        'text_head': text_head,
        'name': name,
        'address': address,
        'phone': phone,
        'mail': mail
    }
    
    return render(request, 'catalog/contact.html', context)


def edit_spare_part(request):
    spare_part = ProductCard.objects.all()
    context = {'spare_part': spare_part}
    
    return render(request, 'catalog/edit_spare_parts.html', context)
        

def add_spare(request):
    if request.method == 'POST':
        form = AddSpareForm(request.POST)
        formset = PhotoFormSet(request.POST, request.FILES, instance=ProductCard())

        if form.is_valid() and formset.is_valid():
            product_card = form.save()

            formset = PhotoFormSet(request.POST, request.FILES, instance=product_card)
            formset.save()

            return redirect('spares')
    else:
        form = AddSpareForm()
        formset = PhotoFormSet(instance=ProductCard())

    context = {'form': form, 'formset': formset}
    return render(request, "catalog/add_spare.html", context)
