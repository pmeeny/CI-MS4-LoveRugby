from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class News(models.Model):
    title = models.CharField(max_length=250, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='news_items')
    news_item_text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_story = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.TextField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create_date']

    def __str__(self):
        return self.comment_text
