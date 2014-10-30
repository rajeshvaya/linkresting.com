from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', "stories.views.index", name="stories.index"),
    url(r'^story/delete/(?P<id>\d+)/?$', "stories.views.delete", name="stories.delete"),
    url(r'^story/(?P<id>\d+)/?$', "stories.views.story", name="stories.story"),
    url(r'^submit', "stories.views.submit", name="stories.submit"),

)