from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Item(models.Model):
    """Модель товара."""
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    currency = models.CharField(
        max_length=3,
        default='USD',
        verbose_name='Валюта',
        help_text='Обозначьте валюту формата "USD, EUR"'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    """Модель заказа."""
    items = models.ManyToManyField(Item, verbose_name='Товары')
    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Общая стоимость',
        default=0
    )
    currency = models.CharField(
        max_length=3,
        default='USD',
        verbose_name='Валюта',
        help_text='Обозначьте валюту формата "USD, EUR"'
    )

    def __str__(self):
        return f"Order {self.id}"

    def calculate_total_cost(self):
        """Вычисляет общую стоимость всех товаров в заказе."""
        return sum(item.price for item in self.items.all())

    def save(self, *args, **kwargs):
        """Переопределяем метод save для расчета общей стоимости."""
        super().save(*args, **kwargs)
        self.total_cost = self.calculate_total_cost()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


@receiver(m2m_changed, sender=Order.items.through)
def update_order_total_cost(sender, instance, action, **kwargs):
    """
    Сигнал для обновления общей стоимости заказа при изменении состава товаров.
    """
    if action in ('post_add', 'post_remove', 'post_clear'):
        # Пересчитываем общую стоимость
        instance.total_cost = instance.calculate_total_cost()
        # Сохраняем заказ
        instance.save()
