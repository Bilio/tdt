from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view/$', views.view_corpus, name='view_corpus'),
    url(r'^addnewtopic/$', views.add_topic, name='add_topic'),
    url(r'^adddocs/$', views.add_docs, name='add_docs'),
    url(r'^addtopic/$', views.addtopic, name='addtopic'),
]