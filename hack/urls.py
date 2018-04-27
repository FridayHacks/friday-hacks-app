from django.conf.urls import url
from . import views

app_name = 'hack'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^propose/$', views.propose, name='propose'),
    url(r'^propose_project/$', views.propose_project, name='propose_project'),
    url(r'^teams/$', views.teams, name='teams')
]
