from django.shortcuts import render,get_object_or_404
from datascraper.models import ProductModel


def productDetail(request, slug):
    product = get_object_or_404(ProductModel,slug=slug)
   
    return render(request, 'pages/productDetail.html', context={
        'product' : product
    })

