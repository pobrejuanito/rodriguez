from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^sendmessage/', views.sendmessage, name='home'),
]
