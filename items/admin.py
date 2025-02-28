from django.contrib import admin
from .models import Order, Item


class OrderAdmin(admin.ModelAdmin):
    """Админка для модели Order."""
    list_display = ('id', 'total_cost', 'currency')
    filter_horizontal = ('items',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
