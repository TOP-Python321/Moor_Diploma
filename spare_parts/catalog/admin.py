from .models import Brands, ModelCar, SparePart, Tires, Rims, SpareState
from django.contrib import admin

# Register your models here.

admin.site.register(Brands)
admin.site.register(ModelCar)
admin.site.register(SparePart)
admin.site.register(Tires)
admin.site.register(Rims)
admin.site.register(SpareState)


