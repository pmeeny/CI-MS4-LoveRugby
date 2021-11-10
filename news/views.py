# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# Internal:
from util.util import setup_pagination
from .forms import NewsForm, CommentForm
from .models import News, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def news_items(request):
    """
    A view to show all news items
    The context contains the news_items_published
    and news_items_drafts
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the news page.
    """
    news_items_published = \
        News.objects.filter(status=1).order_by('-create_date')
    news_items_drafts = \
        News.objects.filter(status=0).order_by('-create_date')

    news_items_published = setup_pagination(news_items_published, request, 4)

    context = {
        'news_items_published': news_items_published,
        'news_items_drafts': news_items_drafts,
    }

    return render(request, 'news/news.html', context)


def manage_news_items(request):
    """
    A view to manage all news items
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the manage news item page.
    """
    all_news_items = News.objects.order_by('-create_date')
    all_news_items = setup_pagination(all_news_items, request, 4)

    context = {
        'news_items': all_news_items,
    }

    return render(request, 'news/manage_news_items.html', context)


@login_required
def add_news_item(request):
    """
    A view to add a news_item
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the add news item page
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


@login_required
def edit_news_item(request, news_item_id):
    """
    A view to editing news items
    Args:
        request (object): HTTP request object.
        news_item_id: News item id
    Returns:
        Renders the edit news item page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    news_item_to_edit = get_object_or_404(News, pk=news_item_id)
    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES,
                             instance=news_item_to_edit)
        if news_form.is_valid():
            news_form.save()
            messages.success(request, f'{news_item_to_edit.title} '
                                      f'was successfully updated')
            return redirect('manage_news_items')
        else:
            messages.error(
                request, f'Error, {news_item_to_edit.title} \
                was not successfully updated')
    else:
        news_form = NewsForm(instance=news_item_to_edit)
        messages.info(request, f'You are currently editing '
                               f'{news_item_to_edit.title}')

    template = 'news/edit_news_item.html'
    context = {
        'news_form': news_form,
        'news_item': news_item_to_edit,
    }

    return render(request, template, context)


@login_required
def delete_news_item(request, news_item_id):
    """
    A view to delete news items
    Args:
        request (object): HTTP request object.
        news_item_id: News item id
    Returns:
        Renders the manage news item after deleting the news item
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    news_item = get_object_or_404(News, pk=news_item_id)
    news_item.delete()
    messages.success(request, f'{news_item.title} Successfully Deleted')
    return redirect(reverse('manage_news_items'))


def news_item(request, news_item_id):
    """
    A view to show an individual news item
    Args:
        request (object): HTTP request object.
        news_item_id: News item id
    Returns:
        Renders the news item page
    """
    news_item = get_object_or_404(News, pk=news_item_id)
    comments = news_item.comments.filter(new_story=news_item_id).\
        order_by('-create_date')
    comments = setup_pagination(comments, request, 2)

    comment = None

    """ Adds comment to new item"""
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.new_story = news_item
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment successfully posted')
            return redirect(reverse('news_item', args=[news_item.id]))
        else:
            messages.error(
                request, 'Comment failed to add, Please retry')
            return redirect(reverse('news_item', args=[news_item.id]))
    else:
        comment_form = CommentForm()

    context = {
        'news_item': news_item,
        'comment_form': comment_form,
        'comments': comments,
        'comment': comment,
    }

    return render(request, 'news/news_item.html', context)


@login_required
def delete_comment(request, comment_id):
    """
    A view to delete news item comments
    Args:
        request (object): HTTP request object.
        comment_id: Comment id
    Returns:
        Renders the edit news item page
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'The comment was deleted')
    return redirect(reverse('news_item', args=[comment.new_story_id]))
