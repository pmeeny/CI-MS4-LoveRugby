from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    return render(request, 'home/index.html', dict(products=products))
