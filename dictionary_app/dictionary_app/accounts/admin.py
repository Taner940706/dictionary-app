from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from dictionary_app.accounts.forms import UserEditForm

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreationForm

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                ),
            }),
        (
            'Personal Info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'picture',
                ),
            },
        ),
        (
            'Permissons',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )
