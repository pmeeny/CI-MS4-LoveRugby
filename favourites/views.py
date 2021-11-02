from django.http import Http404
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from products.models import Product
from .models import Favourites


@login_required
def view_product_favourites(request):
    """
    A view that displays users favourites
    """
    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourites_items = None
    else:
        favourites_items = all_favourites.products.all()

    if not favourites_items:
        messages.info(request, 'Your favourites list is empty!')

    template = 'favourites/favourites.html'
    context = {
        'favourites_items': favourites_items,
    }
    return render(request, template, context)


@login_required
def add_product_to_favourites(request, item_id):
    """
    Add a product item to favourites
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)
    if product in favourites.products.all():
        messages.info(request, 'The product item is '
                               'already in your favourites!')
    else:
        favourites.products.add(product)
        messages.info(request, 'Added product item to your favourites')
    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_product_from_favourites(request, item_id):
    """
    Remove a product item from favourites
    """
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, 'Product item removed '
                               'from your favourites list')
    else:
        messages.error(request, 'That product item is '
                                'not in your favourites list!')
    return redirect(reverse('product_detail', args=[item_id]))
