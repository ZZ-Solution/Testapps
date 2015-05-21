from django.conf.urls import patterns, url
from django.contrib.auth.views import password_reset
urlpatterns = patterns('',
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'accounts/login.html'}
    ),

    url(
        r'^password_change$',
        'django.contrib.auth.views.password_change',
        name='password_change',
        kwargs={
               'template_name': 'accounts/password_change_form.html',
               'post_change_redirect':'accounts:password_reset_complete',
               }
    ),
    url(
        r'^password_reset_complete$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete',
        kwargs={'template_name': 'accounts/password_reset_complete.html'}
    ),

    url(
        r'^password_reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password/reset/done/'},
        name="password_reset"),

        (r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),

        (r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password/done/'}),

        (r'^password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),

    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),

)