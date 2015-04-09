from django.conf.urls import patterns, include, url
from HelloWorldApp.views import foo

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'HelloWorldApp/$', foo), )