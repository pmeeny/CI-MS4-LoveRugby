# Generated by Django 3.2.7 on 2021-11-06 11:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_ratingcomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RatingComment',
            new_name='Review',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rating_text',
            new_name='review_text',
        ),
    ]
