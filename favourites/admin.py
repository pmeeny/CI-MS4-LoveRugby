from django.contrib import admin

from .models import Favourites


class FavouritesAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )


admin.site.register(Favourites, FavouritesAdmin)
