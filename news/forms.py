# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from .models import News, Comment
from products.widgets import CustomClearableFileInput
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class NewsForm(forms.ModelForm):
    """
    A class for the news form
    """
    class Meta:
        model = News
        fields = ('title', 'news_item_text', 'image', 'status')

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """
    A class for the comment form
    """
    class Meta:
        model = Comment
        fields = ('comment_text',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholder
        Args:
            self (object): Self object
            *args: *args
            **kwargs: **kwargs
        Returns:
            N/A
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment_text': 'Add your comment text here',
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1'
            self.fields[field].label = "Comment "

