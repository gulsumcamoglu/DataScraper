from django.shortcuts import render,redirect
from datascraper.forms import link
from datascraper.models import ProductModel


def input(request):
    import requests as r
    from bs4 import BeautifulSoup
    form = link()
    if request.method == 'POST':
        form = link(request.POST)
        if form.is_valid():
            getLink = form.cleaned_data['link']
            res = r.get(getLink)
            soup = BeautifulSoup(res.text,'html.parser')
            title = soup.select("h1.wt-text-body-03")
            product = ProductModel()
            product.name = title[0].get_text()
            img = soup.select(".wt-max-width-full.wt-horizontal-center.wt-vertical-center.carousel-image.wt-rounded")
            for i in img:
                if i["alt"] == "Plant Enthusiast bookmarks image 0":
                     product.img = i["data-src-zoom-image"]
            price = soup.find_all(class_ = 'wt-text-title-03 wt-mr-xs-2')
            product.price = price[0].get_text()
            product.save()
            return redirect('product')


        else:
                print("no")
    context = {
        'form':form
    }
    return render(request, 'pages/input.html',context=context)