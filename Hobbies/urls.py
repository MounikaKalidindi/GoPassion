
from django.conf.urls import url
from django.contrib import admin
from Hobbies import views

urlpatterns = [
	url(r'^q$', views.getDifferentOptions1, name='home'),
   	url(r'^index$', views.index, name='index' ),
   	url(r'^user_home$', views.nav_cat_list, name='user_home'),
   	url(r'^user_home/([\w\s+]+)/(\w+)$', views.getDifferentOptions, name="user_options" ),
   	url(r'^categories$', views.categories_list, name='categories'),
   	#url(r'^categories/(\w+)$', views.getSub_Categories, name='sub_category'),

]
