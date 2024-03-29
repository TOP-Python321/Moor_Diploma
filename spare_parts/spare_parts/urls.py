"""
URL configuration for spare_parts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('spares/', views.SparesListView.as_view(), name='spares'),
    path('spares/<int:pk>/', views.SpareDetailView.as_view(), name='spare-detail'),
    path('spare_detail/<int:pk>/', views.spare_detail, name='spare-detail-custom'),
    path('tires_catalog/', views.show_wheels, name='show_wheels'),
    path('rims_catalog/', views.show_rims, name='show_rims'),
    path('brands/', views.BrandListView.as_view(), name='brands-list'),
    path('brands/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('brand/<int:brand_id>/model/<int:model_id>/', views.model_detail, name='model-parts'),
    path('search/', views.search_parts, name='search-parts'),
    # path('models/<int:pk>/', views.ModelDetailView.as_view(), name='model-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('edit_spare_parts/', views.edit_spare_part, name='edit_spare_parts'),
    path('add_spare/', views.add_spare, name='add_spare'),
    path('delete/<int:id>/', views.delete_spare, name='delete'),
    path('edit_spare/<int:id>/', views.edit_spare, name='edit_spare'),
    path('add_to_cart/<int:spare_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:spare_id>/', views.remove_from_cart, name='remove_from_cart'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# Регистрация входа пользователей
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]    
    