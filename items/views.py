from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
import stripe

from items.models import Item, Order
from test_stripe.settings import (
    STRIPE_SECRET_KEY_EUR,
    STRIPE_SECRET_KEY_USD,
    STRIPE_PUBLISHABLE_KEY_EUR,
    STRIPE_PUBLISHABLE_KEY_USD
)


@require_GET
def buy_item(request, id):
    """Создает Stripe сессию для оплаты одного товара."""
    try:
        item = Item.objects.get(id=id)

        if item.currency == 'USD':
            stripe.api_key = STRIPE_SECRET_KEY_USD
        elif item.currency == 'EUR':
            stripe.api_key = STRIPE_SECRET_KEY_EUR
        else:
            return JsonResponse({'error': 'Unsupported currency'}, status=400)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency,
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://stepaproject.ru/django/success',
            cancel_url='https://stepaproject.ru/django/cancel',
        )
        return JsonResponse({'session_id': session.id})
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


@require_GET
def buy_order(request, id):
    """Создает Stripe сессию для оплаты заказа."""
    try:
        order = Order.objects.get(id=id)

        if order.currency == 'USD':
            stripe.api_key = STRIPE_SECRET_KEY_USD
        elif order.currency == 'EUR':
            stripe.api_key = STRIPE_SECRET_KEY_EUR
        else:
            return JsonResponse({'error': 'Unsupported currency'}, status=400)

        line_items = []
        for item in order.items.all():
            line_items.append({
                'price_data': {
                    'currency': order.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            })

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='https://stepaproject.ru/django/success',
            cancel_url='https://stepaproject.ru/django/cancel',
        )
        return JsonResponse({'session_id': session.id})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)


def item_view(request, id):
    """Отображает страницу товара."""
    try:
        item = Item.objects.get(id=id)
        context = {
            'item': item,
            'STRIPE_PUBLISHABLE_KEY_USD': STRIPE_PUBLISHABLE_KEY_USD,
            'STRIPE_PUBLISHABLE_KEY_EUR': STRIPE_PUBLISHABLE_KEY_EUR,
        }
        return render(request, 'item.html', context)
    except Item.DoesNotExist:
        return render(request, '404.html')


def order_view(request, id):
    """Отображает страницу заказа."""
    try:
        order = Order.objects.get(id=id)
        context = {
            'order': order,
            'STRIPE_PUBLISHABLE_KEY_USD': STRIPE_PUBLISHABLE_KEY_USD,
            'STRIPE_PUBLISHABLE_KEY_EUR': STRIPE_PUBLISHABLE_KEY_EUR,
        }
        return render(request, 'order.html', context)
    except Order.DoesNotExist:
        return render(request, '404.html')


def success_view(request):
    """Страница успешной оплаты."""
    return render(request, 'success.html')


def cancel_view(request):
    """Страница отмены оплаты."""
    return render(request, 'cancel.html')
