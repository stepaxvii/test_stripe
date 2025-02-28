from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django/admin/', admin.site.urls),
    path('django/', include('items.urls')),
]
