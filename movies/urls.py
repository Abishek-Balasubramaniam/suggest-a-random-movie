from django.urls import re_path
from django.contrib import admin
from django.urls import path
from . import views
app_name="movies"
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.movies,name="random_movie")
]
