from django.shortcuts import render
from django.http import HttpResponse
from justwatch import JustWatch
import imdb
import random
def movie_detail(request):
    moviesdb=imdb.IMDb()
    top=moviesdb.get_top250_movies()
    just_watch = JustWatch(country='IN')
    #id_list=[id for id in top[i].getID for i in range(0,250)]
    my_movie=random.choice(top)
    results = just_watch.search_for_item(query=my_movie['title'])
    list = results['items']
    url=[]
    try:
        for item in list[0]['offers']:
            path=item['urls']['standard_web'].split('.')
            if "netflix" in path[1]:
                url.append('Netflix')
            elif "amazon" in path[1]:
                url.append('Amazon prime video')
            elif "prime" in path[1]:
                url.append('Amazon prime video')
            elif "hotstar" in path[1]:
                url.append('Disney+ Hotstar')
            elif "disney" in path[1]:
                url.append('Disney+ Hotstar')
            elif "apple" in path[1]:
                url.append('Apple itunes')
            elif "google" in path[1]:
                url.append('Rent from play-store')
    except KeyError:
        url.append("Couldn't find a streaming service")
    if len(url) == 0:
         url.append("Couldn't find a streaming service")
    
    my_movie['streaming_platforms']=set(url)
    year=my_movie['year']
    tags=(my_movie['title'].lower().split(' '))
    slug=""
    for tag in tags:
        if tag != ':':
            slug+=tag+'-'

    my_movie['free_url1']="https://ww5.fmovie.sc/online/"+slug+str(year)
    my_movie['free_url2']="https://yst.mx/movie/"+slug+str(year)
    movie=moviesdb.get_movie(my_movie.movieID)
    my_movie.genre=movie['genre']
    plot=movie['plot'][0].split('::')
    my_movie.plot=plot[0]
    my_movie.cover_url=movie['cover url']
    my_movie.full_cover_url=movie['full-size cover url']
    my_movie.directors=movie['directors']
    return render(request,'movie_details.html',{'my_movie':my_movie})
    #return HttpResponse(my_movie.genre)