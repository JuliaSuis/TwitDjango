from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.main, name='process'),
    url(r'^search_query$', views.search_query, name='search_query'),
    url(r'^loadImage$', views.loadImagePage, name='loadImagePage'),
]