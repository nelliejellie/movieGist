from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from .forms import movieform,tvShowform
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.db.models import F



# Create your views here.
def hmovies(request):
    movies = Movies.objects.all()
    paginator = Paginator(movies, 10)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)
    context = {
        'movies':paged_movies,
    }
    return render(request,'hollywood/movies.html', context)

def htvshows(request):
    tvshows = Tvshows.objects.all()
    paginator = Paginator(tvshows, 10)
    page = request.GET.get('page')
    paged_tvshows = paginator.get_page(page)
    context = {
        'tvshows':paged_tvshows
    }
    return render(request,'hollywood/tvshows.html', context)
def htvshow(request,htvshow_id):
    tvshow = get_object_or_404(Tvshows, pk= htvshow_id)
    comment = tvshowgist.objects.filter(tvshow=tvshow)
    if request.method == 'POST':
        if request.POST.get('movieGist') == 'worth-seeing':
            gists = request.POST['gist']
            print(request.POST.get('worth-seeing'))
            g = tvshowgist(gists=gists, user=request.user, tvshow=tvshow, worth_seeing=request.POST.get('movieGist'))
            g.save()
            messages.success(request,'your comment was added succesfully')
            return redirect('/htvshows/'+str(htvshow_id))
        elif request.POST.get('movieGist') == 'not-worth-seeing':
            gists = request.POST['gist']
            print(request.POST.get('worth-seeing'))
            g = tvshowgist(gists=gists, user=request.user, tvshow=tvshow, not_worth_seeing=request.POST.get('movieGist'))
            g.save()
            messages.success(request,'your comment was added succesfully')
            return redirect('/htvshows/'+str(htvshow_id))
    context = {
        'tvshow': tvshow,
        'gist':comment
    }       
    return render(request,'hollywood/tvshowDetails.html', context)

def htvshowLike(request):
    gist = get_object_or_404(tvshowgist,id=request.POST.get('comment_id'))
    print(type(request.user))
    gist.gist_like.add(request.user)
    return HttpResponseRedirect(gist.get_absolute_url())
   
def hmovie(request,hmovie_id):
    movie = get_object_or_404(Movies, pk= hmovie_id)
    comment = gist.objects.filter(movie=movie)
    if request.method == 'POST':
        gists = request.POST['gist']
        g = gist(gists=gists, user=request.user, movie=movie)
        g.save()
        messages.success(request,'your comment was added succesfully')
        return redirect('/hmovies/'+str(hmovie_id))
    context = {
        'movie': movie,
        'gist':comment
    }
    return render(request,'hollywood/movieDetails.html', context)
def search(request):
    queryset_list = Movies.objects.order_by('-date')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__iexact=name)

    context = {
        'hmovies': queryset_list,
        'values': request.GET
    }
    return render(request, 'hollywood/search.html', context)


def Mform(request):
    form = movieform(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = movieform(request.POST or None, request.FILES or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('hmovies')
        else:
            print ('error')

    return render(request, 'hollywood/movieform.html',{'form': form})

def Tform(request):
    form = tvShowform(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = tvShowform(request.POST or None, request.FILES or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('htvshows')
        else:
            print ('error')

    return render(request, 'hollywood/tvshowform.html',{'form': form})