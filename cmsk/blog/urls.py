from django.conf.urls import patterns, url

from cmsk.blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.read, name='read'),
    url(r'^archives/$', views.archives, name='archives'),

    )