from django.conf.urls import url
from django.urls import path, include

from . import views
app_name = 'polls'


urlpatterns = [

    url(r'^(?P<pk>)/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #path('', views.index, name='index'),

]