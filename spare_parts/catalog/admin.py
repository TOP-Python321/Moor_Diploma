from .models import Brand, ProductModel, Category, WheelSize, WheelDiameter, ProductCard, Photo, Status, ProductInstance 
from django.contrib import admin
from django.utils.html import format_html


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', )
    list_filter = ('brand_name', )

admin.site.register(Brand, BrandAdmin)

class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance

@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_id', 'brand_id', 'product_model_id', 'vendor_code', 'detail_number')
    list_filter = ('category_id', 'brand_id', 'product_model_id', 'title')
    
    inlines = [ProductInstanceInline]

@admin.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('product_card_id', 'status_id')
    list_filter = ('status_id', )
    
    
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('product_card_id', 'show_photo')
    
    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')
    
    show_photo.short_description = 'Фото'


admin.site.register(ProductModel)
admin.site.register(Category)
admin.site.register(WheelSize)
admin.site.register(WheelDiameter)

admin.site.register(Status)



