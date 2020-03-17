from django.shortcuts import render
from django.http import HttpResponse
from hollywood.models import Movies,Tvshows

# Create your views here.
def index(request):
    hmovies = Movies.objects.order_by('-date')
    context = {
        'hmovies':hmovies
    }
    return render(request, 'pages/index.html', context)

