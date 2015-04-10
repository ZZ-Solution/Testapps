from django.conf.urls import patterns, include, url
from django.contrib import admin
from HelloWorldApp.views import foo, demo 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'HelloWorldApp/$', demo),
    url(r'^admin/', include(admin.site.urls)), )