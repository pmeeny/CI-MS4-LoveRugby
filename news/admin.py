# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import News, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class NewsAdmin(admin.ModelAdmin):
    """
    Admin class for the News model.
    """
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    list_display = (
        'title',
        'user',
        'news_item_text',
        'image',
        'update_date',
        'create_date',
        'status',
    )
    list_filter = (
        'title',
        'user',
        'create_date',
    )
    search_fields = (
        'title',
        'user',
        'news_item_text',
        'image',
        'update_date',
        'create_date',
        'status',
    )
    list_per_page = 20


class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for the Comment model.
    """
    class Meta:
        verbose_name_plural = 'Comments'

    list_display = (
        'user',
        'new_story',
        'comment_text',
        'create_date',
    )
    list_filter = (
        'user',
        'new_story',
        'create_date',
    )
    search_fields = (
        'user',
        'new_story',
        'comment_text',
        'create_date',
    )
    list_per_page = 20


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
