from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        fields = '__all__'
        field_classes = {'username': auth_forms.UsernameField, }


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        fields = ('username', 'email', "password1", "password2")
        field_classes = {'username': auth_forms.UsernameField, }