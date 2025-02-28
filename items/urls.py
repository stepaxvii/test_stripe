from django.urls import path

from items.views import (
    buy_item,
    buy_order,
    cancel_view,
    item_view,
    order_view,
    success_view
)

urlpatterns = [
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('item/<int:id>/', item_view, name='item_view'),
    path('buy_order/<int:id>/', buy_order, name='buy_order'),
    path('order/<int:id>/', order_view, name='order_view'),
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
]
