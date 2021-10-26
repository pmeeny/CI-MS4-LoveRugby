from django.contrib import admin
from .models import News, Comment


class NewsAdmin(admin.ModelAdmin):

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
        'status',
    )


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'new_story',
        'comment_text',
        'create_date',
    )

admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
