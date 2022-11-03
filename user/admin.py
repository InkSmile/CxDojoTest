from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomAdmin(UserAdmin):
    model = User


    add_fieldsets = (
        (None, {
                
                "fields": ("username", "password1", "password2", 'first_name', 'last_name', 'avatar'),
            },
        ),
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'first_name', 'last_name', 'date_joined', 'avatar')
        }),
        
    )