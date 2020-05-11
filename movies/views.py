from django.shortcuts import render
from django.http import HttpResponse
import imdb
import random
def movies(request):
    moviesdb=imdb.IMDb()
    top=moviesdb.get_top250_movies()
    #id_list=[id for id in top[i].getID for i in range(0,250)]
    my_movie=random.choice(top)
    movie=moviesdb.get_movie(my_movie.movieID)
    my_movie.genre=movie['genre']
    plot=movie['plot'][0].split('::')
    my_movie.plot=plot[0]
    my_movie.cover_url=movie['cover url']
    my_movie.full_cover_url=movie['full-size cover url']
    my_movie.directors=movie['directors']
    return render(request,'movie_details.html',{'my_movie':my_movie})
    #return HttpResponse(my_movie.genre)