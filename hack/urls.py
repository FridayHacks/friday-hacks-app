from django.conf.urls import url
from . import views

app_name = 'hack'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^teams/$', views.teams, name='teams')
]
