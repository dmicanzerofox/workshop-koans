from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^create_widget/$', views.create_widget_view, name='create_widget'),
]
