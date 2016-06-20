from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from . import views
from books import views as bkviews

books_patterns = [
    url(r'^books/$', bkviews.search),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    url(r'^$', views.my_homepage_view),

    # url(r'^search/$', bkviews.search),
    # include other url_patterns
    url(r'^search/', include(books_patterns)),

    url(r'^contact/$', views.contact),

    # include other app's urls.py
    url(r'^samples/', include('samples.urls')),

    url(r'^namespace/', include('samples.urls', namespace='author-reviews', app_name='samples')),

]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug), ]
