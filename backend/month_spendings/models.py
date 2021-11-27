from datetime import datetime

from django.db import models

P = models.PROTECT


class Month(models.Model):
    year = models.IntegerField(null=False)
    month = models.IntegerField(null=False)

    max_spending = models.IntegerField(null=False, default=0)

    @property
    def spent(self) -> int:
        return sum(s.value for s in self.spending_set.all())

    @property
    def name(self) -> str:
        return [
            'Январь',
            'Февраль',
            'Март',
            'Апрель',
            'Май',
            'Июнь',
            'Июль',
            'Август',
            'Сентябрь',
            'Октябрь',
            'Ноябрь',
            'Декабрь',
        ][self.month - 1]

    @property
    def full_name(self) -> str:
        return '{} {}'.format(self.name, self.year)

    @property
    def is_current(self) -> bool:
        now = datetime.now()
        return self.year == now.year and self.month == now.month

    @property
    def balance(self):
        return self.max_spending - self.spent

    @classmethod
    def make_current(cls, max_spending):
        now = datetime.now()
        return cls(year=now.year, month=now.month, max_spending=max_spending)

    class Meta:
        unique_together = ('year', 'month')


class SpendCategory(models.Model):
    name = models.CharField(max_length=255, null=False)


class Spending(models.Model):
    name = models.CharField(max_length=255, null=False)
    month = models.ForeignKey(Month, on_delete=P, null=False)
    category = models.ForeignKey(SpendCategory, on_delete=P, null=False)
    value = models.IntegerField(null=False)
