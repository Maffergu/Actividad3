from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graf',views.graf,name='graf'),
]