from django.urls import path

from dictionary_app.dictionary.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]