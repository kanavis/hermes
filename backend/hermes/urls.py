"""hermes URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

import month_spendings.views

urlpatterns = [
    path('', month_spendings.views.show_months),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
