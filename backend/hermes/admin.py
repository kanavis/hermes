from django.contrib import admin

from month_spendings.models import SpendCategory


class SpendCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


admin.site.register(SpendCategory, SpendCategoryAdmin)
