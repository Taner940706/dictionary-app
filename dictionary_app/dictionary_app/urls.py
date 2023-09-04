from django.contrib import admin
from django.urls import path, include

from dictionary_app.dictionary.views import View500, View404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('dictionary_app.dictionary.urls')),
    path('', include('dictionary_app.accounts.urls')),
]

handler404 = View404.as_view()
handler500 = View500.as_view()
