from django.urls import path
from . import views

urlpatterns = [
    path('nollywood/search',views.search, name='search'),
    path('nmovies/',views.nmovies, name='nmovies'),
    path('ntvshows/',views.ntvshows, name='ntvshows'),
    path('nmovies/<int:nmovie_id>',views.nmovie, name='nmovie'),
    path('ntvshows/<int:ntvshow_id>',views.ntvshow, name='ntvshow'),
    path('ntvshows/Tform',views.Tform, name='Tform'),
    path('nmovies/Mform',views.Mform, name='Mform'),
    
]