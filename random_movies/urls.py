from django.urls import re_path
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'random_movies'


urlpatterns = [
    re_path(r'marked/',views.marked,name="marked"),
    re_path(r'^$',views.movie_detail,name='random_movie'),
   #re_path(r'accounts/',include('accounts.urls')),
    re_path(r'^mark/$',views.mark,name='mark'),
    url(r'^(?P<movie_title>[\w\s\:\-]+)/$',views.remove,name="remove_marked"),
]
