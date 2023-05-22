from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('dictionary_app.dictionary.urls')),
    path('', include('dictionary_app.accounts.urls')),
]

handler404 = 'dictionary_app.dictionary_app.View404'
handler500 = 'dictionary_app.dictionary_app.View500'
