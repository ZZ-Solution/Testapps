from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.conf import settings#for photo upload
from django.conf.urls.static import static#for photo upload

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
	url(r'^$', 'polls.views.hello_world'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^change/password/$','accounts.views.change_password', name='changepassword'),
]