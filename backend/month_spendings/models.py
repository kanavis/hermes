from django.db import models

P = models.PROTECT


class Month(models.Model):
    year = models.IntegerField(null=False)
    month = models.IntegerField(null=False)

    max_spending = models.IntegerField(null=False, default=0)

    class Meta:
        unique_together = ('year', 'month')


class SpendCategory(models.Model):
    name = models.CharField(max_length=255, null=False)


class Spending(models.Model):
    name = models.CharField(max_length=255, null=False)
    month = models.ForeignKey(Month, on_delete=P, null=False)
    category = models.ForeignKey(SpendCategory, on_delete=P, null=False)
    value = models.IntegerField(null=False)
