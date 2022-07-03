"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^index',index,name="index"),
   
   url(r'^adminhome',adminhome,name="adminhome"),
   url(r'^alogout',alogout,name="alogout"),
   url(r'^login',login,name="login"),
    url(r'^adminupload',adminupload,name="adminupload"),
    url(r'^adminview',adminview,name="adminview"),
    url(r'^upload',upload,name="upload"),
    url(r'^check1',check1,name="check1"),
    url(r'^downloadfile1',downloadfile1,name="downloadfile1"),
    url(r'^adminchecks',adminchecks,name="adminchecks"),





   


]
