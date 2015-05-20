from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'polls.views.hello_world'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
]