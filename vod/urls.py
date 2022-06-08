from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda x: redirect('/admin')),
    path('admin/', admin.site.urls),
    path('vod_api/', include('core.urls')),
]
