from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from dictionary_app.accounts.forms import UserCreateForm

UserModel = get_user_model()


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
        return super().form_invalid(form)


class RegisterView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserEditView(views.UpdateView):
    template_name = 'accounts/user-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'picture')

    def get_success_url(self):
        return reverse_lazy('login')


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete.html'
    model = UserModel


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')



