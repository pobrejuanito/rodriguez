from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.english, name='home-en'),
    url(r'^es/', views.spanish, name='home-es'),
    url(r'^sendmessage/', views.sendmessage, name='home-en'),
]
