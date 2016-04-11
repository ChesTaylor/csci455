from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^elections/', include('elections.urls')),
    url(r'^admin/', admin.site.urls),
]