from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^moneyadder/$', views.moneyadder, name='moneyadder'),
]
