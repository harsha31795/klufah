"""Atevents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import  settings
from django.contrib import admin
from django.urls import path
from Atapp.views import *

urlpatterns = [
    url("captcha/", include('captcha.urls')),
    url("accounts/", include("django.contrib.auth.urls")),
    url("^register/", register, name="register"),
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('home/', index,name="index"),
    path('about/', about,name="about"),
    path('contact/', contact,name="contact"),
    path('services/', services,name="services"),
    path('team/', team,name="team"),
    path('gallery/', gallery,name="gallery"),
    path('faqs/', faqs,name="faqs"),
    path('terms/', terms,name="terms"),
    path('signin/', signin,name="signin"),
    path('signup/', register,name="signup"),
    path('signout/', signout,name="signout"),
    path('dashboard/', dashboard,name="dashboard"),
    path('thanks/', thanks,name="thanks"),
    path('new/', new,name="new"),
    path('profile/', profile, name = 'profile'),
    path('myevents/', myevents, name = 'myevents'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    url('delete/(?P<pk>[0-9]+)/$', delete,name="delete"),
]


    
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


