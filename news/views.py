from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import NewsForm
from .models import News


def news_items(request):
    """
    A view to show all news items
    The context contains the news_items_published
    and news_items_drafts
    """

    news_items_published = News.objects.filter(status=1).order_by('-create_date')
    news_items_drafts = News.objects.filter(status=0).order_by('-create_date')

    context = {
        'news_items_published': news_items_published,
        'news_items_drafts': news_items_drafts,
    }

    return render(request, 'news/news.html', context)

def manage_news_items(request):
    """
    A view to manage all news items
    """
    news_items = News.objects.order_by('-create_date')

    context = {
        'news_items': news_items,
    }

    return render(request, 'news/manage_news_items.html', context)

@login_required
def add_news_item(request):
    """
    A view to add a news_item
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES)
        if news_form.is_valid():
            form_data = news_form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.success(request, 'Your news item was posted successfully!')
            return redirect('news_items')
        else:
            messages.error(
                request, 'Your news item failed to add, Please try again')
            return redirect('add_news_item')
    else:
        news_form = NewsForm()

    template = 'news/add_news_item.html'
    context = {
        'post_form': news_form,
    }
    return render(request, template, context)
