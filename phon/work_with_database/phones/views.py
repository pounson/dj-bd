from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'id')
    sort_by = {
        'min_price': 'price',
        'name': 'name',
        'max_price': '-price'
        }
    template = 'catalog.html'
    data = Phone.objects.all().order_by(sort_by.get(sort, 'id'))
    context = {'phones': data}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
        }
    return render(request, template, context)