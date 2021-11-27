"""hermes URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

import month_spendings.views

urlpatterns = [
    path('', month_spendings.views.show_months),
    path(
        'month/spendings/<int:year>/<int:month>',
        month_spendings.views.show_month_spendings,
        name='show_month_spendings',
    ),
    path(
        'month/spendings/add/<int:year>/<int:month>',
        month_spendings.views.add_month_spending,
        name='add_month_spending',
    ),
    path(
        'month/max_spending/edit/<int:year>/<int:month>',
        month_spendings.views.edit_max_spending,
        name='edit_max_spending',
    ),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
