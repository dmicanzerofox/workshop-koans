from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^correct_types/$', views.correct_types, name='correct_types'),
]
