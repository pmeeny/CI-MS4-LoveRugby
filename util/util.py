# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def setup_pagination(item_list, request, items_per_page):
    """
    This function setups pagination, with items per page
    :return paginated item_list object
    """
    paginator = Paginator(item_list, items_per_page)
    page = request.GET.get('page', 1)
    try:
        item_list = paginator.page(page)
    except PageNotAnInteger:
        item_list = paginator.page(1)
    except EmptyPage:
        item_list = paginator.page(paginator.num_pages)
    return item_list
