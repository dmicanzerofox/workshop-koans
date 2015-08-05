from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^create_widget/$', views.create_widget_view, name='create_widget'),
    url(r'^unicode/$', views.unicode_test, name='unicode_test'),
    url(r'^utc/$', views.utc_conversion_test, name='utc_conversion_test'),
]
