from django.urls import path
from . import views

urlpatterns = [
    path('bollywood/search-bmovie',views.search, name='search-bmovie'),
    path('bollywood/search-btvshow',views.search_btvshow, name='search-btvshow'),
    path('bmovies/',views.bmovies, name='bmovies'),
    path('btvshows/',views.btvshows, name='btvshows'),
    path('bmovies/<int:bmovie_id>',views.bmovie, name='bmovie'),
    path('btvshows/<int:btvshow_id>',views.btvshow, name='btvshow'),
    path('btvshows/Tform',views.Tform, name='bTform'),
    path('bmovies/Mform',views.Mform, name='bMform'),
    path('bmovies/<int:bmovie_id>/delete',views.Bdelete, name='bdelete'),
    path('btvshows/<int:btvshow_id>/deletetvshow',views.BdeleteTvshow, name='bdeletetvshow'),
    path('btvshows/<int:btvshow_id>/deletetvshowthread',views.bTvshowThreadDelete, name='bTvshowThreadDelete'),
    path('bmovies/<int:bmovie_id>/deletemoviethread',views.bmovieDelete, name='bmoviesdelete'),
]