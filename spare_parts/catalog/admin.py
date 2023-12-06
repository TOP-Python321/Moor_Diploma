from .models import Brand, ProductModel, Category, WheelSize, WheelDiameter, ProductCard, Photo, Status, ProductInstance 
from django.contrib import admin

# Register your models here.

admin.site.register(Brand)
admin.site.register(ProductModel)
admin.site.register(Category)
admin.site.register(WheelSize)
admin.site.register(WheelDiameter)
admin.site.register(Photo)
admin.site.register(ProductCard)
admin.site.register(Status)
admin.site.register(ProductInstance)


