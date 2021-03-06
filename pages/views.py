from django.shortcuts import render, redirect
from django.http import HttpResponse
from hollywood.models import Movies,Tvshows
from bollywood.models import Movies as bollyMov
from bollywood.models import Tvshows as bollyTv
from nollywood.models import Movies as nollyMov
from nollywood.models import Tvshows as nollyTv
from .models import contact,VideoClips,VideoClips1,VideoClips2,VideoClips3
from django.contrib import messages,auth
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    hmovies = Movies.objects.order_by('-date')[:3]
    bmovies = bollyMov.objects.order_by('-date')[:3]
    nmovies = nollyMov.objects.order_by('-date')[:3]
    htvshows = Tvshows.objects.order_by('-date')[:3]
    ntvshows = nollyTv.objects.order_by('-date')[:3]
    btvshows = bollyTv.objects.order_by('-date')[:3]
    myclip =  VideoClips.objects.order_by('-id')
    myclip1 =  VideoClips1.objects.order_by('-id')
    myclip2 =  VideoClips2.objects.order_by('-id')
    myclip3 =  VideoClips3.objects.order_by('-id')


    context = {
        'hmovies':hmovies,
        'bmovies':bmovies,
        'nmovies':nmovies,
        'htvshows' : htvshows,
        'ntvshows' : ntvshows,
        'btvshows' : btvshows,
        'myclip' : myclip,
        'myclip1' : myclip1,
        'myclip2' : myclip2,
        'myclip3' : myclip3,

    }
    return render(request, 'pages/index.html', context)

def contacts(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phone_no = request.POST['mobile']
        email = request.POST['email']
        description = request.POST['description']
        form = contact(fullname=fullname, phone_no=phone_no, email=email, description=description, user=request.user)
        form.save()
        messages.success(request, 'your message has been sent successfully')
        return redirect('contact')

    return render(request, 'pages/contactus.html')


def howtouse(request):
    return render(request, 'pages/about.html')