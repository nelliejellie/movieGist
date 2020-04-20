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
    movies = Movies.objects.order_by('-date')
    paginator = Paginator(movies, 30)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)
    context = {
        'movies':paged_movies,
    }
    return render(request,'nollywood/movies.html', context)

def ntvshows(request):
    tvshows = Tvshows.objects.order_by('-date')
    paginator = Paginator(tvshows, 30)
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
            if gist.objects.filter(tvshow=tvshow, user_id=request.user.id).exists():
                messages.error(request, 'you already commented on this tvshow')
            else:
                gists = request.POST['gist']
                print(request.POST.get('worth-seeing'))
                g = tvshowgist(gists=gists, user=request.user, tvshow=tvshow, worth_seeing=request.POST.get('movieGist'))
                g.save()
                l= Like(user=request.user, tvshow=tvshow)
                l.save()
                messages.success(request,'your comment was added succesfully')
                return redirect('/ntvshows/'+str(ntvshow_id))
        elif request.POST.get('movieGist') == 'not-worth-seeing':
            if gist.objects.filter(tvshow=tvshow, user_id=request.user.id).exists():
                messages.error(request, 'you already commented on this tvshow')
            else:
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
    movie = get_object_or_404(Movies, pk= nmovie_id)
    comment = gist.objects.filter(movie=movie)
    like = MovieLike.objects.filter(movie=movie)
    dislike = MovieDislike.objects.filter(movie=movie)
    if request.method == 'POST':
        if request.POST.get('movieGist') == 'worth-seeing':
            if gist.objects.filter(tvshow=tvshow, user_id=request.user.id).exists():
                messages.error(request, 'you already commented on this movie')
            else:
                gists = request.POST['gist']
                print(request.POST.get('worth-seeing'))
                g = gist(gists=gists, user=request.user, movie=movie, worth_seeing=request.POST.get('movieGist'))
                g.save()
                l= MovieLike(user=request.user, movie=movie)
                l.save()
                messages.success(request,'your comment was added succesfully')
                return redirect('/nmovies/'+str(nmovie_id))
        elif request.POST.get('movieGist') == 'not-worth-seeing':
            if gist.objects.filter(tvshow=tvshow, user_id=request.user.id).exists():
                messages.error(request, 'you already commented on this movie')
            else:
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
def search_nmovies(request):
    queryset_list = Movies.objects.order_by('-date')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)

    context = {
        'nmovies': queryset_list,
        'values': request.GET
    }
    return render(request, 'nollywood/search-nmovie.html', context)

def search_ntvshow(request):
    queryset_list = Tvshows.objects.order_by('-date')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)

    context = {
        'ntvshows': queryset_list,
        'values': request.GET
    }
    return render(request, 'nollywood/search-ntvshow.html', context)


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
            item.user= request.user
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
                item.user= request.user
                item.save()
                return redirect('ntvshows')
        else:
            messages.error(request,'the tvshow exists already, try searching')

    return render(request, 'nollywood/tvshowform.html',context)

def Ndelete(request, nmovie_id):
    gists = get_object_or_404(gist, id=nmovie_id)
    movie  = Movies.objects.filter(gist=gists)
    like = MovieLike.objects.filter(user=request.user,movie=gists.movie) 
    dislike = MovieDislike.objects.filter(user=request.user, movie=gists.movie)   
    if request.method == 'POST':
        if request.POST.get('comment') == 'Yes':
            if gists.user == request.user:
                gists.delete()
                if like:
                    like.delete()
                else:
                    dislike.delete()
                messages.success(request,'your comment was deleted successfully')
                return redirect('/nmovies/')
            else:
                messages.error(request,'this comment could not be deleted because you werent the creator')
    context = {
        'movie' : movie,
        'gists' : gists,
    }
    return render(request,'nollywood/delete.html', context)

def NdeleteTvshow(request, ntvshow_id):
    tvshowgists = get_object_or_404(tvshowgist, id=ntvshow_id)
    tvshow  = Tvshows.objects.filter(tvshowgist=tvshowgists)
    like = Like.objects.filter(user=request.user,tvshow=tvshowgists.tvshow) 
    dislike = Dislike.objects.filter(user=request.user, tvshow=tvshowgists.tvshow)   
    if request.method == 'POST':
        if request.POST.get('comment') == 'Yes':
            if tvshowgists.user == request.user:
                tvshowgists.delete()
                if like:
                    like.delete()
                else:
                    dislike.delete()
                messages.success(request,'your comment was deleted successfully')
                return redirect('/ntvshows/')
            else:
                messages.error(request,'this comment could not be deleted because you werent the creator')
    context = {
        'tvshow' : tvshow,
        'tvshowgists' : tvshowgists,
    }
    return render(request,'nollywood/deletetvshow.html', context)


def nmovieDelete(request, nmovie_id):
    deleteMovie = get_object_or_404(Movies, id=nmovie_id)
    if request.method == 'POST':
        if request.POST.get('comment') == 'Yes':
            if deleteMovie.user == request.user:
                deleteMovie.delete()
                messages.success(request,'your movie thread was deleted successfully')
                return redirect('nmovies')
            else:
                messages.error(request,'this movie could not be deleted because you werent the creator')
    context = {
        'deleteMovie' : deleteMovie,
    }
    return render(request,'nollywood/delMovie.html', context)

def nTvshowThreadDelete(request, ntvshow_id):
    deletetvshow = get_object_or_404(Tvshows, id=ntvshow_id)
    if request.method == 'POST':
        if request.POST.get('comment') == 'Yes':
            if deletetvshow.user == request.user:
                deletetvshow.delete()
                messages.success(request,'your tvshow thread was deleted successfully')
                return redirect('nmovies')
            else:
                messages.error(request,'this tvshow could not be deleted because you werent the creator')
    context = {
        'deletetvshow' : deletetvshow,
    }
    return render(request,'nollywood/deltvshow.html', context)


