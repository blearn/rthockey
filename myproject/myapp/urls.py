from django.conf.urls import patterns, url

#from django.conf import settings
#from django.conf.urls.static import static

from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^program/(?P<program_id>\d+)/$', views.program, name='program'),
    url(r'^session/(?P<session_id>\d+)/$', views.session, name='session'),
    url(r'^register_session/(?P<session_id>\d+)/$', views.register_session, name='register_session'),
    url(r'^register_program/(?P<program_id>\d+)/$', views.register_program, name='register_program'),
    url(r'^programs/$', views.selectProgram, name='programs'),
    url(r'^gallery/$', views.gallery, name='gallery'),
#    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^player/$', views.player, name='player'),
#    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
