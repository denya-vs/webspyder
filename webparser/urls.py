from django.conf.urls import patterns, url

from webparser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^parse/$', views.parse, name='parse'),
)