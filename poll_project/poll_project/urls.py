"""poll_project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from polly import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.poll_home, name = 'poll_home'),
    path('create/', views.poll_create, name ='poll_create'),
    path('results/<pol_id>/', views.poll_results, name ='poll_results'),
    path('vote/<pol_id>/', views.poll_vote, name ='poll_vote'),
    path('vote/', views.poll_vote1, name ='poll_vote1'),
]
