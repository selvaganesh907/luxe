"""
URL configuration for luxesalon_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from salon import views   # adjust myapp to your app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),        
    path('services/', views.services, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('booknow/', views.booknow, name='booknow'),
]