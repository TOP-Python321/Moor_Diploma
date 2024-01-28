from django.contrib import admin
from django.urls import path, include
from .import views


urlpattern = [
    path('', views.index, name='index'), 
    path('spares/', views.SparesListView.as_view(), name='spares'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('spare_parts.urls')),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
]