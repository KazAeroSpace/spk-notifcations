from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from apps.request.views import webhook

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/user/', include('apps.user.urls')),
    path('api/v1/contract/', include('apps.contract.urls')),
]
