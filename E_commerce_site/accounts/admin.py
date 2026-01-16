from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'username', 'first_name', 'last_name',
        'phone_number', 'is_active', 'is_staff', 'is_superuser'
    )
    list_display_links = ('email', 'username')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'username', 'phone_number')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name',
                'phone_number', 'password1', 'password2',
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )

    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(Account, AccountAdmin)

# admin.site.register(Account)

# admin.site.unregister(Group)  # If you want to unregister the Group model