from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    # ex: /elections/
    url(r'^$', login_required(views.index), name='index'),
    # ex: /elections/5/
    url(r'^(?P<candidate_id>[0-9]+)/$', login_required(views.detail), name='detail'),
    # ex: /elections/5/results/
    url(r'^(?P<candidate_id>[0-9]+)/results/$', login_required(views.results), name='results'),
    # ex: /elections/5/vote/
    url(r'^(?P<candidate_id>[0-9]+)/vote/$', login_required(views.vote), name='vote'),
]