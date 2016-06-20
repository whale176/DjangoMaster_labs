from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^form/', include([
        url(r'^requestPath/$', views.current_url_view_good),
        url(r'^uadisplay1/$', views.ua_display_good1),
        url(r'^uadisplay2/$', views.ua_display_good2),
        url(r'^displayMeta/$', views.display_meta),
    ])),
    url(r'reviews/', include([
        url(r'^$', views.page),
        url(r'^page(?P<num>[0-9]+)/$', views.page),
        url(r'^fix/(?P<year>[0-9]{4})/$', views.fixed_year, {'year': '2010'}),
        url(r'^([0-9]{4})/$', views.year_archive, name='reviews-year-archive'),

    ])),
    url(r'^archive/$', views.archive),
    url(r'^about/$', views.about),
    url(r'^namespace/', views.show_namespace),

    # url(r'^category/(?P<cat_name>\w+)/$', views.category),
    # Reverse resolution of URLs
    # url(r'^category/(?P<cat_name>\w+)/$', views.category, name='list_category'),

]
