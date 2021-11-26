from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


@login_required
def show_months(request: HttpRequest):
    render(request, 'months_spendings/months.html')
