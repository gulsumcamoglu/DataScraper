from django.urls import path
from datascraper.views import product,input



urlpatterns = [
    path('',input),
    path('product',product),
]
