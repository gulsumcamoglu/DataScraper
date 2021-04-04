from django.shortcuts import render


def input(request):
    return render(request, 'pages/input.html',context={})