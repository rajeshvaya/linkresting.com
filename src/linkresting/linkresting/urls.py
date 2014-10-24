from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/signin/$', 'auth.views.signin', name='auth.signin'),
    url(r'^auth/signup/$', 'auth.views.signup', name='auth.signup'),
    url(r'^auth/signout/$', 'auth.views.signout', name='auth.signout'),
    url(r'^auth/$', 'auth.views.auth', name="auth"),
    
    url(r'', include('stories.urls')),
)