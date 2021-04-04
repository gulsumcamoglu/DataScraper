from django.shortcuts import render
from datascraper.models import ProductModel
from django.core.paginator import Paginator

def product(request):
    products = [1,2,3,4]
    page = request.GET.get('page')
    paginator = Paginator(products,2)

    return render(request, 'pages/product.html',context={
        'products':paginator.get_page(page)
    })

