from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'HelloWorld.hello.hello_world'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]