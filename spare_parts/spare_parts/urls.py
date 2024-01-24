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
    path('spares/', views.SparesListView.as_view(), name='spares'),
    path('spares/<int:pk>/', views.SpareDetailView.as_view(), name='spare-detail'),
    path('brands/', views.BrandListView.as_view(), name='brands-list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('edit_spare_parts/', views.edit_spare_part, name='edit_spare_parts'),
    path('add_spare/', views.add_spare, name='add_spare'),
    path('delete/<int:id>/', views.delete_spare, name='delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# Регистрация входа пользователей
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]    
    