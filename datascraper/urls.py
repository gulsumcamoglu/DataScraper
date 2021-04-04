from django.urls import path
from datascraper.views import product,input



urlpatterns = [
    path('',input,name = 'input'),
    path('product',product, name = 'product'),
]
