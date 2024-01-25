from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import ProductCard, Category, Brand, ProductModel, WheelSize, WheelDiameter, Photo

class AddSpareForm(forms.ModelForm):
    class Meta:
        model = ProductCard
        fields = ['title', 'category_id', 'brand_id', 'product_model_id', 'wheel_size_id', 'wheel_diameter_id', 'vendor_code', 'detail_number', 'description', 'price']

    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория товара")

    brand_id = forms.CharField(label='Бренд', required=False)
    product_model_id = forms.CharField(label='Модель', required=False)
    wheel_size_id = forms.CharField(label='Размер шины', required=False)
    wheel_diameter_id = forms.CharField(label='Диаметр колеса', required=False)

    def clean_brand_id(self):
        brand_name = self.cleaned_data.get('brand_id')
        if brand_name:
            brand, created = Brand.objects.get_or_create(brand_name=brand_name)
            return brand
        else:
            raise forms.ValidationError('Введите бренд.')

    def clean_product_model_id(self):
        model_name = self.cleaned_data.get('product_model_id')
        if model_name:
            brand_id = self.cleaned_data.get('brand_id')
            model, created = ProductModel.objects.get_or_create(brand_id=brand_id, model_name=model_name)
            return model
        else:
            return None

    def clean_wheel_size_id(self):
        size = self.cleaned_data.get('wheel_size_id')
        if size:
            wheel_size, created = WheelSize.objects.get_or_create(size=size)
            return wheel_size
        else:
            return None

    def clean_wheel_diameter_id(self):
        diameter = self.cleaned_data.get('wheel_diameter_id')
        if diameter:
            wheel_diameter, created = WheelDiameter.objects.get_or_create(diameter=diameter)
            return wheel_diameter
        else:
            return None

PhotoFormSet = inlineformset_factory(ProductCard, Photo, fields=('photo',), extra=3)


class EditSpareForm(forms.ModelForm):
    class Meta:
        model = ProductCard
        fields = '__all__'


class DeleteSpareForm(forms.Form):
    confirm = forms.BooleanField(label='Вы уверены, что хотите удалить эту запчасть?', required=True)
    
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    