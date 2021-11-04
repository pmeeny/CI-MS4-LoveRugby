from django import forms
from .models import News, Comment
from products.widgets import CustomClearableFileInput


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'news_item_text', 'image', 'status')

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_text',)
        labels = {
            'comment_text': '',
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholder and remove auto-generated labels """
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment_text': 'Add your comment text here and click the Post '
                            'Comment button',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1'
            self.fields[field].label = "Comment "

