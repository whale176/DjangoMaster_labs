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
    url(r'^search/', include(books_patterns)),
    url(r'^contact/$', views.contact),
    url(r'^reviews/$', views.page),
    url(r'^reviews/page(?P<num>[0-9]+)/$', views.page),
    url(r'^samples/', include('samples.urls'))
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug), ]
