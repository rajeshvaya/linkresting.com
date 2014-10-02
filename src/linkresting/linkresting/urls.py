from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from django.shortcuts import render_to_response


def design_index(request):
	return render_to_response('design/index.html')


urlpatterns = patterns('',
    # Examples:
    url(r'^$', design_index),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)