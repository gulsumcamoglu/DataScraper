from django.urls import path
from datascraper.views import product,input,productDetail



urlpatterns = [
    path('',input,name = 'input'),
    path('product',product, name = 'product'),   
    path('productDetail/?P<slug:slug>',productDetail, name= 'productDetail'),

]
