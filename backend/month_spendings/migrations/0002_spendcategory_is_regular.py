# Generated by Django 3.2.9 on 2021-12-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('month_spendings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spendcategory',
            name='is_regular',
            field=models.BooleanField(default=False),
        ),
    ]
