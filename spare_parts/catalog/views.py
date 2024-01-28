from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from .forms import AddSpareForm, PhotoFormSet, EditSpareForm, DeleteSpareForm, CustomUserCreationForm
from .models import ProductCard, Photo, Brand, Cart, CartItem


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

            photos = formset.save(commit=False)
            for photo in photos:
                photo.product_card_id = product_card
                photo.save()

            return redirect('spares')
    else:
        form = AddSpareForm()
        formset = PhotoFormSet(instance=ProductCard())

    context = {'form': form, 'formset': formset}
    return render(request, "catalog/add_spare.html", context)


def delete_spare(request, id):
    try:
        spare_part = ProductCard.objects.get(id=id)
        spare_part.delete()
        return HttpResponseRedirect("/edit_spare_parts/")
    except:
        return HttpResponseNotFound("<h2>Запчасть не найдена</h2>")


def edit_spare(request, id):
    spare_part = ProductCard.objects.get(id=id)
    
    if request.method == "POST":
        instance = ProductCard.objects.get(pk=id)
        form = EditSpareForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/edit_spare_parts/")
    else:
        form = EditSpareForm(instance=spare_part)
        
    photos = spare_part.photos.all()
    content = {"form": form, "photos": photos}
    return render(request, "catalog/edit_spare.html", content)


def delete_spare(request, id):
    spare_part = get_object_or_404(ProductCard, id=id)

    if request.method == "POST":
        delete_form = DeleteSpareForm(request.POST)

        if delete_form.is_valid() and delete_form.cleaned_data['confirm']:
            spare_part.delete()
            return HttpResponseRedirect("/edit_spare_parts/")

    else:
        delete_form = DeleteSpareForm()

    context = {"spare_part": spare_part, "delete_form": delete_form}
    return render(request, "catalog/delete_confirm.html", context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def add_to_cart(request, spare_id):
    spare = get_object_or_404(ProductCard, id=spare_id)
    user_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
    cart_item, item_created = CartItem.objects.get_or_create(cart=user_cart, product=spare)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('spare-detail', pk=spare_id)


def view_cart(request):
    user_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
    cart_items = user_cart.cartitem_set.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})