from django.contrib import admin
from . import models


@admin.register(models.Contract)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['oid', 'num', 'exp_date', 'phone_num']
    list_filter = ['region',]

    list_display = ('id',
                    'region',
                    'oid',
                    'user',
                    'exp_date',
                    'num',
                    'phone_num',
                    'payment_date',
                    'last_payment_date',
                    )
    