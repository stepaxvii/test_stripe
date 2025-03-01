# Test Stripe
## Этот проект демонстрирует интеграцию Django с Stripe для обработки платежей.

# Описание проекта
## Проект включает в себя:

- Базовую административную панель Django.

- Интеграцию с Stripe для тестирования платежей.

- Поддержку мультивалютных платежей (USD и EUR).

# Запуск проекта с помощью Docker
## Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/stepaxvii/test_stripe.git
```
## Шаг 2: Переход в директорию проекта
```bash
cd test_stripe
```
## Шаг 3: Запуск контейнеров
```bash
docker-compose -f docker-compose.production.yml up -d
```
## Шаг 4: Доступ к проекту

Основной сайт: https://stepaproject.ru/django/

Админка: https://stepaproject.ru/django/admin/

## Шаг 5: Остановка контейнеров
```
bash
docker-compose down
```
# Настройка проекта
## Переменные окружения
Храните конфиденциальные данные в файле .env. Пример содержимого файла .env:
```
env
DEBUG=False
SECRET_KEY=your_secret_key_here
STRIPE_PUBLISHABLE_KEY_USD=your_stripe_publishable_key_here
STRIPE_SECRET_KEY_USD=your_stripe_secret_key_here
STRIPE_PUBLISHABLE_KEY_EUR=your_stripe_publishable_key_here
STRIPE_SECRET_KEY_EUR=your_stripe_secret_key_here
ALLOWED_HOSTS=127.0.0.1,localhost
```
# Настройка Stripe
## Получите API-ключи Stripe:

- Publishable Key (для фронтенда).

- Secret Key (для бэкенда).

## Убедитесь, что ключи для USD и EUR настроены в .env.

# Настройка Nginx
## Убедитесь, что Nginx настроен для обслуживания статических файлов и проксирования запросов к Django. Пример конфигурации:
```
nginx
Copy
server {
    listen 80;
    server_name stepaproject.ru;

    location /django {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location /django/static/ {
        alias /app/staticfiles/;
    }
}
```
# Использование
- Создание товаров: Используйте админку Django для добавления товаров и заказов.

- Оплата: Перейдите на страницу товара и нажмите "Купить". Вы будете перенаправлены на страницу оплаты Stripe.

- Тестирование: Используйте тестовые карты Stripe для проверки платежей.

# Локализация
## Проект поддерживает мультивалютные платежи (USD и EUR). Убедитесь, что товары созданы с правильной валютой.

# Логи и отладка
## Логи Django: Проверьте логи контейнера Django:
```
bash
docker logs django_app_prod
```
## Логи Nginx: Проверьте логи Nginx для диагностики проблем со статикой:
```
bash
sudo tail -f /var/log/nginx/error.log
```
# Автор
## Автор: Игорь Степаненко

## Репозиторий: https://github.com/stepaxvii/test_stripe

# Примечания
## Убедитесь, что все зависимости установлены и настроены.

- Для production-режима установите DEBUG=False в .env.