from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import app, index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('users.urls')),
    url(r'^app/', app, name='app'),
    url('^auth/login/$', login, name='login'),
    url('^auth/logout/$', logout_then_login, name='logout'),
    url('^$', index, name='index'),

]

urlpatterns += staticfiles_urlpatterns()

