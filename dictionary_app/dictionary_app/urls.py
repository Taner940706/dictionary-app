from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('dictionary_app.dictionary.urls')),
    path('', include('dictionary_app.accounts.urls')),
]
