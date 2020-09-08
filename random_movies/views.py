from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from justwatch import JustWatch
from .models import Movie
import imdb
import random
def movie_detail(request):
    moviesdb=imdb.IMDb()
    top=moviesdb.get_top250_movies()
    #just_watch = JustWatch(country='IN')
    #id_list=[id for id in top[i].getID for i in range(0,250)]
    my_movie=random.choice(top)
    #results = just_watch.search_for_item(query=my_movie['title'])
    list = results['items']
    url=[]
    """try:

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
    
    except IndexError:
        return redirect('random_movies:random_movie')
    
    if len(url) == 0:
         url.append("Couldn't find a streaming service")
    my_movie['streaming_platforms']=set(url)
    if "Amazon prime video" in url and "Netflix" in url:
        aapp="Netflix and Amazon prime video"
    elif "Amazon prime video" in url:
        aapp="Amazon prime"
    elif "Netflix" in url:
        aapp="Netflix"
    elif "Disney+ Hotstar" in url:
        aapp="Disney+ Hotstar"
    elif "Rent from play-store" in url:
        aapp="Rent from play-store"
    elif "Apple itunes" in url:
        aapp="Apple itunes"
    elif "Couldn't find a streaming service" in url:
        aapp="Couldn't find a streaming service"""
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
    request.session['url']=movie['full-size cover url']
    request.session['title']=my_movie['title']
    #request.session['avail_on']=aapp
    return render(request,'movie_details.html',{'my_movie':my_movie})
    #return HttpResponse(my_movie.genre)
  
def marked(request):
     movies=Movie.objects.filter(author=request.user)
     return render(request,'marked.html',{'movies':movies})

@login_required
def mark(request):
    mtitle=request.session['title']
    murl=request.session['url']
    #mavail_on=request.session['avail_on']
    Movie.objects.create(title=mtitle,url=murl,author=request.user)
    return redirect('random_movies:random_movie')

def remove(request,movie_title):
    #mtitle=movie_name
    #mtitle1=mtitle.pop()
    Movie.objects.filter(author=request.user).filter(title=movie_title).delete()
    return redirect('random_movies:marked')
