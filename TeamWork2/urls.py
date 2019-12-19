"""TeamWork2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from index.views import index, login, register
from search_record.views import search_record

#jojo的女兒們
from django.urls import include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #path('index/login/', login),
    #path('index/register/', register),
    path('search_record/', search_record),

    #path('index/login/', TemplateView.as_view(template_name='home.html')),
    path('', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
]


