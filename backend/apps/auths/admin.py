from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
        Custom user admin
    """
    list_display = (
        'email',
        'surname',
        'name',
        'patronymic',
        'is_active',
    )
    list_filter = ('email', )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2')
        }),
        ('Personal info', {
            'classes': ('wide', ),
            'fields': ('surname', 'name', 'patronymic', 'token')
        }),
        ('Permissions', {
            'classes': ('wide', ),
            'fields': ('is_active', 'is_staff', 'is_superuser')
        })
    )
    fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'classes': ('wide', ),
            'fields': ('surname', 'name', 'patronymic', 'token')
        }),
        ('Permissions', {
            'classes': ('wide', ),
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Other fields', {
            'classes': ('wide', ),
            'fields': ('activate_code', 'date_of_creation', 'date_of_change')
        })
    )
    readonly_fields = (
        'activate_code', 'date_of_creation', 'date_of_change', 'is_superuser'
    )
    search_fields = ('email', )
    ordering = ('email', )


admin.site.register(CustomUser, CustomUserAdmin)
