from django.contrib import admin
from . import models


@admin.register(models.Contract)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['oid', 'num', 'exp_date', 'phone_num']

    list_display = ('id',
                    'oid', 'num', 'exp_date', 'phone_num'
                    )
    