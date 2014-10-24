from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', "stories.views.index", name="stories.index"),
    url(r'^submit', "stories.views.submit", name="stories.submit"),
)