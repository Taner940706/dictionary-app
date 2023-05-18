from django.urls import path

from dictionary_app.dictionary.views import Home

urlpatterns = (
    path('', Home.as_view(), name='home'),
)