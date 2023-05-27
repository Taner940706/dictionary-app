from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib import messages
from dictionary_app.accounts.forms import UserCreateForm

UserModel = get_user_model()


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Username and/or password is incorrect!")
        return super().form_invalid(form)


class RegisterView(SuccessMessageMixin, views.CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    success_message = "User is sign up successfully!"

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def form_invalid(self, form):
        if form['password1'].value() != form['password2'].value():
            messages.error(self.request, "Passwords doesn't match")
        else:
            messages.error(self.request, "Username exist!!")
        return super().form_invalid(form)


class UserEditView(SuccessMessageMixin, views.UpdateView):
    template_name = 'accounts/user-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'picture')
    success_message = "User was updated successfully"

    def get_success_url(self):
        return reverse_lazy('login')


class UserDeleteView(SuccessMessageMixin, views.DeleteView):
    template_name = 'accounts/user-delete.html'
    model = UserModel
    success_message = "User was deleted successfully"


class SignOutView(SuccessMessageMixin, auth_views.LogoutView):
    next_page = reverse_lazy('login')
    success_message = "User was logged out successfully"



