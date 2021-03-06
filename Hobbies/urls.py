from django.conf.urls import url
from django.contrib import admin
from Hobbies import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
   	url(r'^index$', views.index, name='index' ),
   	url(r'^user_home$', views.nav_cat_list, name='user_home'),
   	url(r'^user_home/([0-9]+)/([0-9]+)$', views.getDifferentOptions, name="user_options" ),

    url(r'^q$', views.getDifferentOptions1, name='home'),
    url(r'^index$', views.index, name='index'),
    url(r'^user_home$', views.nav_cat_list, name='user_home'),
    url(r'^user_home/([0-9]+)/([0-9]+)/$', views.getDifferentOptions, name="user_options"),
    url(r'^categories$', views.categories_list, name='categories'),
    # url(r'^categories/(\w+)$', views.getSub_Categories, name='sub_category'),
    url(r'^user_home/([1-9]+)/([1-9]+)/addPost$', views.addpost, name='addpost')
]
