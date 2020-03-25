from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from .forms import movieform,tvShowform
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.db.models import F



# Create your views here.
def nmovies(request):
    movies = Movies.objects.all()
    paginator = Paginator(movies, 10)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)
    context = {
        'movies':paged_movies,
    }
    return render(request,'nollywood/movies.html', context)

def ntvshows(request):
    tvshows = Tvshows.objects.order_by('-date')
    paginator = Paginator(tvshows, 10)
    page = request.GET.get('page')
    paged_tvshows = paginator.get_page(page)
    context = {
        'tvshows':paged_tvshows,
    }
    return render(request,'nollywood/tvshows.html', context)
def ntvshow(request,ntvshow_id):
    tvshow = get_object_or_404(Tvshows, pk= htvshow_id)
    comment = tvshowgist.objects.filter(tvshow=tvshow)
    like = Like.objects.filter(tvshow=tvshow)
    dislike = Dislike.objects.filter(tvshow=tvshow)
    if request.method == 'POST':
        if request.POST.get('movieGist') == 'worth-seeing':
            gists = request.POST['gist']
            print(request.POST.get('worth-seeing'))
            g = tvshowgist(gists=gists, user=request.user, tvshow=tvshow, worth_seeing=request.POST.get('movieGist'))
            g.save()
            l= Like(user=request.user, tvshow=tvshow)
            l.save()
            messages.success(request,'your comment was added succesfully')
            return redirect('/ntvshows/'+str(ntvshow_id))
        elif request.POST.get('movieGist') == 'not-worth-seeing':
            gists = request.POST['gist']
            print(request.POST.get('worth-seeing'))
            g = tvshowgist(gists=gists, user=request.user, tvshow=tvshow, not_worth_seeing=request.POST.get('movieGist'))
            g.save()
            dl = Dislike(user=request.user, tvshow=tvshow)
            dl.save()
            messages.success(request,'your comment was added succesfully')
            return redirect('/ntvshows/'+str(ntvshow_id))
    context = {
        'tvshow': tvshow,
        'gist':comment,
        'like':like,
        'dislike':dislike
    }       
    return render(request,'nollywood/tvshowDetails.html', context)

def ntvshowLike(request):
    tvshowLike = get_object_or_404(Tvshows,id=request.GET.get('like'))
    tvshowLike.like.add(request.user)
    return HttpResponseRedirect(tvshowLike.get_absolute_url())
   
def nmovie(request,nmovie_id):
    movie = get_object_or_404(Movies, pk= hmovie_id)
    comment = gist.objects.filter(movie=movie)
    like = MovieLike.objects.filter(movie=movie)
    dislike = MovieDislike.objects.filter(movie=movie)
    if request.method == 'POST':
        if request.POST.get('movieGist') == 'worth-seeing':
            gists = request.POST['gist']
            print(request.POST.get('worth-seeing'))
            g = gist(gists=gists, user=request.user, movie=movie, worth_seeing=request.POST.get('movieGist'))
            g.save()
            l= MovieLike(user=request.user, movie=movie)
            l.save()
            messages.success(request,'your comment was added succesfully')
            return redirect('/nmovies/'+str(nmovie_id))
        elif request.POST.get('movieGist') == 'not-worth-seeing':
            gists = request.POST['gist']
            print(request.POST.get('worth-seeing'))
            g = gist(gists=gists, user=request.user, movie=movie, not_worth_seeing=request.POST.get('movieGist'))
            g.save()
            dl = MovieDislike(user=request.user, movie=movie)
            dl.save()
            messages.success(request,'your comment was added succesfully')
            return redirect('/nmovies/'+str(nmovie_id))
    context = {
        'movie': movie,
        'gist':comment,
        'like':like,
        'dislike':dislike
    }       
    return render(request,'nollywood/movieDetails.html', context)
def search(request):
    queryset_list = Movies.objects.order_by('-date')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__iexact=name)

    context = {
        'nmovies': queryset_list,
        'values': request.GET
    }
    return render(request, 'nollywood/search.html', context)


def Mform(request):
    form = movieform(request.POST or None, request.FILES or None)
    queryset = Movies.objects.all()
    context = {
        'form':form,
        'queryset':queryset
    }
    if form.is_valid():
        name = form.cleaned_data['name']
        if Movies.objects.filter(name=name).exists():
            return redirect('nmovies')
        else:
            item = form.save(commit=False)
            item.save()
            return redirect('nmovies')
    else:
        messages.error(request,'the movie exists already, try searching')

    return render(request, 'nollywood/movieform.html',context)

def Tform(request):
    form = tvShowform(request.POST or None, request.FILES or None)
    queryset = Tvshows.objects.all()
    context = {
        'form':form,
        'queryset':queryset
    }
    if request.method == 'POST':
        form = tvShowform(request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Tvshows.objects.filter(name=name).exists():
                return redirect('ntvshows')
            else:
                item = form.save(commit=False)
                item.save()
                return redirect('ntvshows')
        else:
            messages.error(request,'the tvshow exists already, try searching')

    return render(request, 'nollywood/tvshowform.html',context)