from django.contrib import admin
from django.urls import path
from .views import hello
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
