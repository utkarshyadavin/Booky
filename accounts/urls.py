from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout


app_name = 'accounts'

urlpatterns= [

url(r'^$', views.home, name='home'),
url(r'^(?P<category_id>[0-9]+)/$', views.information, name='information'),
#url(r'^add/$', views.add, name='add'),
#surl(r'^browse/$', views.browse, name='browse')

]