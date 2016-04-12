from django.conf.urls import include, url
from django.contrib import admin
from elections import views

urlpatterns = [
    url(r'^elections/', include('elections.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.user_login, name='login')
]