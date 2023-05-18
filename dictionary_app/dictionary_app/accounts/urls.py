from django.urls import path, include

from dictionary_app.accounts.views import LoginView, RegisterView, SignOutView, UserEditView, UserDeleteView

urlpatterns = (
    path('', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)