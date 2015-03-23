from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /myapp/5/
    url(r'^program/(?P<program_id>\d+)/$', views.program, name='program'),
    url(r'^session/(?P<session_id>\d+)/$', views.session, name='session'),
)
