from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course, Enrollment, Module


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'role', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Module)
