from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect

from month_spendings.models import Month, SpendCategory, Spending

MAX_SPENDING_DEFAULT = 30000
SPENDINGS_FORM_LEN = 10


def redir_message(url, message):
    url = url + '?' + urlencode(dict(message=message))
    return redirect(url)


@login_required
def show_months(request: HttpRequest):
    q = Month.objects.all()
    months = list(q.prefetch_related('spending_set').order_by('-year', '-month')[:5])
    if not (months and months[0].is_current):
        max_spending = months[0].max_spending if months else MAX_SPENDING_DEFAULT
        curr_month = Month.make_current(max_spending=max_spending)
        curr_month.save()
        months.insert(0, curr_month)

    context = dict(
        months=months,
        message=request.GET.get('message'),
    )
    return render(request, 'months_spendings/months.html', context)


def obtain_month(year: int, month: int) -> Month:
    try:
        return Month.objects.get(year=year, month=month)
    except Month.DoesNotExist:
        raise Http404('Month doesn\'t exist')


@login_required
def show_month_spendings(request: HttpRequest, year: int, month: int):
    month = obtain_month(year, month)
    context = dict(
        month=month,
        spendings=month.spending_set.all(),
    )
    return render(request, 'months_spendings/spendings.html', context)


@login_required
def add_month_spending(request: HttpRequest, year: int, month: int):
    month = obtain_month(year, month)
    if request.method == 'POST':
        added = 0
        for name, category_id, value in zip(
            request.POST.getlist('name'),
            request.POST.getlist('category'),
            request.POST.getlist('value'),
        ):
            if name:
                added += 1
                spending = Spending(
                    name=name,
                    category_id=int(category_id),
                    value=int(value),
                    month=month,
                )
                spending.save()
        return redir_message('/', 'Добавлено {} расходов'.format(added))
    else:
        categories = list(SpendCategory.objects.all().order_by('pk'))
        context = dict(
            month=month,
            form_gen=range(SPENDINGS_FORM_LEN),
            categories=categories,
        )
        return render(request, 'months_spendings/add_spending.html', context)


@login_required
def edit_max_spending(request: HttpRequest, year: int, month: int):
    month = obtain_month(year, month)
    if request.method == 'POST':
        max_spending = int(request.POST.get('max_spending'))
        month.max_spending = max_spending
        month.save()
        return redir_message('/', 'Настройки сохранены')
    else:
        context = dict(month=month)
        return render(request, 'months_spendings/edit_max_spendings.html', context)
