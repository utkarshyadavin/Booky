from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout


app_name = 'accounts'

urlpatterns= [

url(r'^$', views.home, name='home'),
url(r'^browse$', views.browse, name='browse'),
url(r'^register/$', views.register, name='register'),
url(r'^login/$',login, {'template_name': 'accounts/login.html'}),
url(r'^logout/$', logout,{'template_name': 'accounts/logout.html'}),
url(r'^(?P<category_id>[0-9]+)/$', views.information, name='information'),
url(r'^category/add/$', views.CategoryCreate.as_view(), name='category-add'),
url(r'^(?P<category_id>[0-9]+)/information/add/$', views.InfoCreate.as_view(), name='information-add'),
url(r'^redirect1/$', views.category_added, name='category_added'),
url(r'^redirect2/$', views.information_added, name='information_added'),
url(r'^(?P<category_id>[0-9]+)/(?P<element_id>[0-9]+)/$', views.description, name='information'),


#surl(r'^browse/$', views., name='browse')

]
