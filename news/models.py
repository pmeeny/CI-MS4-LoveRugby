# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class News(models.Model):
    """
    This model is for a news item
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=250,
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news_items'
    )
    news_item_text = models.TextField()
    image = models.ImageField(
        null=True,
        blank=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    This model is for a news item comment
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    new_story = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    comment_text = models.TextField(
        verbose_name=_('Comment Text'),
        null=False,
        blank=False
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['create_date']

    def __str__(self):
        return self.comment_text
