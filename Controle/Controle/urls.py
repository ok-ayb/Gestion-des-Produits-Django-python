
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ouakki_ayoub/', include('ouakki_ayoub.urls')),
]

