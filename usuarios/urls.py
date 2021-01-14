from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cadastro', views.cadastro),
    path('login',views.login),
    path('logout',views.login),
    path('dashboard',views.dashboard),

] 
