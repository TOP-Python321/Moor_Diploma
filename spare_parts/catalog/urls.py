from django.urls import path
from .import views


urlpattern = [
    path('', views.index, name='index'), 
    path('spares/', views.SparesListView.as_view(), name='spares'),
]