from django.conf.urls import patterns, url
from mango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^test/', views.test, name = 'test'),
)
