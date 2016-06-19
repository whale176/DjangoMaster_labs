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
]
