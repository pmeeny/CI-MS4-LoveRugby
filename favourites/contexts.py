# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.http import Http404
from django.shortcuts import get_object_or_404

# Internal:
from .models import Favourites
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def wishlist_contents(request):
    """
    A context for Favourites to display count in users navbar
    """
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
        favourites_items = favourites.products.all()
        favourites_count = len(favourites_items)
    except Http404:
        favourites_count = None

    context = {
        'favourites_count': favourites_count,
    }

    return context
