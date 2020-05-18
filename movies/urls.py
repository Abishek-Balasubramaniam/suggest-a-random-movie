from django.urls import re_path
from django.contrib import admin
from django.urls import path,include
from random_movies import views as movie_view

app_name = 'movies'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',movie_view.movie_detail,name='random_movie'),
    #re_path(r'^marked/$',views.marked,name="marked"),
    #re_path(r'random_movie/',views.movie_detail,name='random_movie'),
    re_path(r'^accounts/',include('accounts.urls')),
    re_path(r'^random_movies/',include('random_movies.urls')),
    #re_path(r'mark',views.mark),
   
]
