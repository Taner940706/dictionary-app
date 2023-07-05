from django.urls import path

from dictionary_app.dictionary.views import HomeView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
]