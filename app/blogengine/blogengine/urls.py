from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls'))]


admin.site.site_header = settings.ADMIN_SITE_HEADER
