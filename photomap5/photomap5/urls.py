from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('photo/', include('photo.urls')),
    path('', include('account.urls')),
]
