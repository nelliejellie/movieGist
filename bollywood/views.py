from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from .forms import movieform,tvShowform
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.db.models import F



# Create your views here.
def bmovies(request):
    movies = Movies.objects.all()
    paginator = Paginator(movies, 10)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)
    context = {
        'movies':paged_movies,
    }
    return render(request,'bollywood/movies.html', context)

def btvshows(request):
    tvshows = Tvshows.objects.order_by('-date')
    paginator = Paginator(tvshows, 10)
    page = request.GET.get('page')
    paged_tvshows = paginator.get_page(page)
    context = {
        'tvshows':paged_tvshows,
    }
    return render(request,'bollywood/tvshows.html', context)
def btvshow(request,btvshow_id):
    tvshow = get_object_or_404(Tvshows, pk= btvshow_id)
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
                return redirect('/btvshows/'+str(btvshow_id))
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
                return redirect('/btvshows/'+str(btvshow_id))
    context = {
        'tvshow': tvshow,
        'gist':comment,
        'like':like,
        'dislike':dislike
    }       
    return render(request,'bollywood/tvshowDetails.html', context)

def btvshowLike(request):
    tvshowLike = get_object_or_404(Tvshows,id=request.GET.get('like'))
    tvshowLike.like.add(request.user)
    return HttpResponseRedirect(tvshowLike.get_absolute_url())
   
def bmovie(request,bmovie_id):
    movie = get_object_or_404(Movies, pk= bmovie_id)
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
                return redirect('/bmovies/'+str(bmovie_id))
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
                return redirect('/bmovies/'+str(bmovie_id))
    context = {
        'movie': movie,
        'gist':comment,
        'like':like,
        'dislike':dislike
    }       
    return render(request,'bollywood/movieDetails.html', context)
def search(request):
    queryset_list = Movies.objects.order_by('-date')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__iexact=name)

    context = {
        'bmovies': queryset_list,
        'values': request.GET
    }
    return render(request, 'bollywood/search.html', context)

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
            return redirect('bmovies')
        else:
            item = form.save(commit=False)
            item.save()
            return redirect('bmovies')
    else:
        messages.error(request,'the movie exists already, try searching')

    return render(request, 'bollywood/movieform.html',context)

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
                return redirect('btvshows')
            else:
                item = form.save(commit=False)
                item.save()
                return redirect('btvshows')
        else:
            messages.error(request,'the tvshow exists already, try searching')

    return render(request, 'bollywood/tvshowform.html',context)

def Bdelete(request, bmovie_id):
    gists = get_object_or_404(gist, id=bmovie_id)
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
                return redirect('/bmovies/')
            else:
                messages.error(request,'this comment could not be deleted because you werent the creator')
    context = {
        'movie' : movie,
        'gists' : gists,
    }
    return render(request,'bollywood/delete.html', context)

def BdeleteTvshow(request, btvshow_id):
    tvshowgists = get_object_or_404(tvshowgist, id=btvshow_id)
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
                return redirect('/btvshows/')
            else:
                messages.error(request,'this comment could not be deleted because you werent the creator')
    context = {
        'tvshow' : tvshow,
        'tvshowgists' : tvshowgists,
    }
    return render(request,'bollywood/deletetvshow.html', context)