from django.contrib import admin
from django.urls import path
from apps.app_views import views

urlpatterns = [
    path('pc/index', views.index, name='index'),
    path('admin/', admin.site.urls),
]
