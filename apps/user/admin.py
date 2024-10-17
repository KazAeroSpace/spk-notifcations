from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'last_name',
                     'first_name', 'email', 'iin',
                     'tg_chat_id'
                     ]
    list_filter = ['groups', 'is_staff', 'is_superuser', 'is_blocked', ]
    date_hierarchy = "date_joined"
    list_display = ('id',
                    'is_blocked',
                    'tg_chat_id',
                    'username',
                    'last_name',
                    'first_name',
                    'patronymic',
                    'email',
                    'iin',
                    'groups_names',
                    'date_joined'
                    )
    readonly_fields = [
        'password',
        'user_permissions',
        'date_joined',
        'last_login',
        'is_superuser'
    ]
