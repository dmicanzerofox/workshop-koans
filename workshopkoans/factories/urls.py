from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^post_retriever/$', views.post_retriever, name='post_retriever'),
]
