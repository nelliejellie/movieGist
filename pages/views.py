from django.shortcuts import render, redirect
from django.http import HttpResponse
from hollywood.models import Movies,Tvshows
from bollywood.models import Movies as bollyMov
from bollywood.models import Tvshows as bollyTv
from nollywood.models import Movies as nollyMov
from nollywood.models import Tvshows as nollyTv
from .models import contact
from django.contrib import messages,auth
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    hmovies = Movies.objects.order_by('-date')
    bmovies = bollyMov.objects.order_by('-date')
    nmovies = nollyMov.objects.order_by('-date')
    htvshows = Tvshows.objects.order_by('-date')
    ntvshows = nollyTv.objects.order_by('-date')
    btvshows = bollyTv.objects.order_by('-date')

    context = {
        'hmovies':hmovies,
        'bmovies':bmovies,
        'nmovies':nmovies,
        'htvshows' : htvshows,
        'ntvshows' : htvshows,,
        'btvshows' : htvshows,
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