from django import forms
from django.forms import Textarea
from .widgets import CustomClearableFileInput
from .models import Product, Category, User, RatingComment


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductRatingCommentForm(forms.ModelForm):
    """
    Represents a form for product rating and comments
    """
    class Meta:
        """
        Fields and types for product rating and comments form.
        """
        model = RatingComment
        fields = (
            'product_rating',
            'rating_text',
        )

        widgets = {
            'product_rating': forms.Select(attrs={'id': 'choice'}),
            'rating_text': Textarea(attrs={'rows': 4}),
        }
