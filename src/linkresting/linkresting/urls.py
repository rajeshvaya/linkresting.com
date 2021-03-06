from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/signin/$', 'auth.views.signin', name='auth.signin'),
    url(r'^auth/signup/$', 'auth.views.signup', name='auth.signup'),
    url(r'^auth/signout/$', 'auth.views.signout', name='auth.signout'),
    url(r'^auth/forgot/initialized/$', 'auth.views.forgot_initialized', name='auth.forgot_initialized'),
    url(r'^auth/forgot/$', 'auth.views.forgot', name='auth.forgot'),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^auth/$', 'auth.views.auth', name="auth"),
    
    url(r'', include('stories.urls')),

    url('', include('social.apps.django_app.urls', namespace='social')), # social login
    url('', include('django.contrib.auth.urls', namespace='auth')),

    url(r'^info/about$', TemplateView.as_view(template_name="info/about.html"), name="info.about"),
    url(r'^info/github$', TemplateView.as_view(template_name="info/github.html"), name="info.github"),
    url(r'^info/inspire$', TemplateView.as_view(template_name="info/inspire.html"), name="info.inspire"),


    url(r'^.*$', 'stories.views.index'), # default page for 404 not found
)