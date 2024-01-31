from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.urls import reverse
from typing import Union
from .forms import AddSpareForm, PhotoFormSet, EditSpareForm, DeleteSpareForm, CustomUserCreationForm
from .models import ProductCard, Photo, Brand, Cart, CartItem, ProductModel


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
    template_name = 'catalog/brand_list.html' 


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'catalog/brand_detail.html'
    context_object_name = 'brand'
    
    
@login_required
def spare_detail(request, pk):
    spare = get_object_or_404(ProductCard, pk=pk)
    is_in_cart = False

    user_cart, _ = Cart.objects.get_or_create(user_id=request.user.id)
    is_in_cart = user_cart.cartitem_set.filter(product=spare).exists()

    if request.method == "POST":
        form = AddSpareForm(request.POST)
        if form.is_valid():
            cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=spare)

            if not created:
                cart_item.quantity += 1
                cart_item.save()

            return redirect('add_to_cart', spare_id=spare.id)

    else:
        form = AddSpareForm()

    context = {
        'spare': spare,
        'is_in_cart': is_in_cart,
        'form': form,
    }

    return render(request, 'catalog/spare_detail.html', context)


def index(request) -> HttpResponse:
    """
    Отображение главной страницы каталога запчастей.

    :param request: HttpRequest

    :return: HttpResponse
    """
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


def show_wheels(request) -> HttpResponse:
    """
    Отображение всех доступных шин.

    :param request: HttpRequest

    :return: HttpResponse
    """
    text_head = 'Каталог шин'
    tires = ProductCard.objects.filter(category_id=2)
    num_tires = ProductCard.objects.filter(category_id=2).count()
    brand = Brand.objects
    photo = Photo.objects.all()
    
    context = {
        'text_head': text_head,
        'tires': tires,
        'num_tires': num_tires,
        'brand': brand,
        'photo': photo
    }
    
    return render(request, 'catalog/tires_catalog.html', context)


def show_rims(request) -> HttpResponse:
    """
    Отображение всех доступных дисков.

    :param request: HttpRequest

    :return: HttpResponse
    """
    text_head = 'Каталог дисков'
    rims =  ProductCard.objects.filter(category_id=3)
    num_rims = ProductCard.objects.filter(category_id=3).count()
    brand = Brand.objects
    photo = Photo.objects.all()
    
    context = {
        'text_head': text_head,
        'rims': rims,
        'num_rims': num_rims,
        'brand': brand,
        'photo': photo
    }
    
    return render(request, 'catalog/rims_catalog.html', context)


def model_detail(request, brand_id, model_id) -> HttpResponse:
    """
    Отображение доступных запчастей модели.

    :param request: HttpRequest
    :param brand_id: объект бренда
    :param model_id: объект модели

    :return: HttpResponse
    """
    brand = get_object_or_404(Brand, id=brand_id)
    model = get_object_or_404(ProductModel, id=model_id)
    spare_parts = ProductCard.objects.filter(brand_id=brand.id, product_model_id=model.id)

    context = {
        'brand': brand,
        'model': model,
        'spare_parts': spare_parts,
    }

    return render(request, 'catalog/model_parts.html', context)
    
    

def about(request) -> HttpResponse:
    """
    Отображение страницы 'О компании'
    
    :param request: HttpRequest

    :return: HttpResponse
    """
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
   
   
def contact(request) -> HttpResponse:
    """
    Отображение страницы 'Контакты'
    
    :param request: HttpRequest

    :return: HttpResponse
    """
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


def edit_spare_part(request) -> HttpResponse:
    """
    Отображение страницы для редактирования запчасти из каталога
    
    :param request: HttpRequest

    :return: HttpResponse
    """
    spare_part = ProductCard.objects.all()
    context = {'spare_part': spare_part}
    
    return render(request, 'catalog/edit_spare_parts.html', context)


def add_spare(request) -> HttpResponse:
    """
    Отображение страницы для добавление запчасти
    
    :param request: HttpRequest

    :return: HttpResponse
    """
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


def delete_spare(request, id: int) -> HttpResponse:
    """
    Удаление запчасти по идентификатору
    
    :param request: HttpRequest
    :param id: int, идентификатор запчасти 

    :return: HttpResponse
    """
    try:
        spare_part = ProductCard.objects.get(id=id)
        spare_part.delete()
        return HttpResponseRedirect("/edit_spare_parts/")
    except:
        return HttpResponseNotFound("<h2>Запчасть не найдена</h2>")


def edit_spare(request, id: int) -> HttpResponse:
    """
    Редактирование запчасти

    :param request: HttpRequest
    :param id: int, идентификатор запчасти 

    :return: HttpResponse
    """
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


def delete_spare(request, id: int) -> HttpResponse:
    """
    Удаление запчасти

    :param request: HttpRequest
    :param id: int, идентификатор запчасти 

    :return: HttpResponse
    """
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


def register(request) -> HttpResponse:
    """
    Регистрация пользователя

    :param request: HttpRequest

    :return: HttpResponse
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def add_to_cart(request, spare_id: int) -> Union[HttpResponse, None]:
    """
    Добавление товара в корзину пользователя.

    :param request: HttpRequest
    :param spare_id: идентификатор запчасти

    :return: В случае успешного добавления возвращает None, происходит перенаправление на страницу деталей запчасти.
    """
    spare = get_object_or_404(ProductCard, id=spare_id)
    user_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
    cart_item, item_created = CartItem.objects.get_or_create(cart=user_cart, product=spare)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('spare-detail', pk=spare_id)


@login_required
def view_cart(request) -> HttpResponse:
    """
    Отображение корзины

    :param request: HttpRequest

    :return: HttpResponse
    """
    user_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
    cart_items = user_cart.cartitem_set.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, spare_id):
    user_cart, _ = Cart.objects.get_or_create(user_id=request.user.id)
    spare = get_object_or_404(ProductCard, id=spare_id)
    cart_item = CartItem.objects.get(cart=user_cart, product=spare)
    cart_item.delete()

    return redirect('view_cart')