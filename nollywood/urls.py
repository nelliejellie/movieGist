from django.urls import path
from . import views

urlpatterns = [
    path('nollywood/search-nmovie',views.search, name='search-nmovie'),
    path('bollywood/search-ntvshow',views.search_ntvshow, name='search-ntvshow'),
    path('nmovies/',views.nmovies, name='nmovies'),
    path('ntvshows/',views.ntvshows, name='ntvshows'),
    path('nmovies/<int:nmovie_id>',views.nmovie, name='nmovie'),
    path('ntvshows/<int:ntvshow_id>',views.ntvshow, name='ntvshow'),
    path('ntvshows/Tform',views.Tform, name='Tform'),
    path('nmovies/Mform',views.Mform, name='Mform'),
    path('nmovies/<int:nmovie_id>/delete',views.Ndelete, name='ndelete'),
    path('ntvshows/<int:ntvshow_id>/deletetvshow',views.NdeleteTvshow, name='ndeletetvshow'),
    path('ntvshows/<int:ntvshow_id>/deletetvshowthread',views.nTvshowThreadDelete, name='nTvshowThreadDelete'),
    path('nmovies/<int:nmovie_id>/deletemoviethread',views.nmovieDelete, name='nmoviesdelete'),
]