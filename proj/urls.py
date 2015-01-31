from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.index, name='index'),
    url(r'^claim/$', views.claim, name='claim'),
    url(r'^action/$', views.action, name='action'),
    url(r'^alias/$', views.alias, name='alias'),
    url(r'^statement/$', views.index, name='statement'),
    url(r'^people/$', views.people, name='people'),
    url(r'^$', RedirectView.as_view(pattern_name='statement')),
)