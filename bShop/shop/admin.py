from django.contrib import admin
from .models import Item, ItemCategory


class ItemAdmin(admin.ModelAdmin):
    # fields = ['name', 'description', 'price']

    list_display = ('name', 'description', 'price', 'category')

    list_filter = ['category']

    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory)
