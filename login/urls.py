from django.conf.urls import patterns, include, url
from login import views

urlpatterns = patterns('',
                       url(r'^$', views.login),
                       url(r'^profile/$', views.profile),
                       url(r'^clock_in/$', views.clockin),
                       )
