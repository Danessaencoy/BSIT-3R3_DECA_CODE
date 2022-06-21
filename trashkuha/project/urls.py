from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('app_user/', include('django.contrib.auth.urls')),
    path('app_user/', include('app_user.urls')),
    
]
