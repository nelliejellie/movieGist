from django.urls import path
from . import views

urlpatterns = [
    path('hollywood/search',views.search, name='search'),
    path('hmovies/',views.hmovies, name='hmovies'),
    path('htvshows/',views.htvshows, name='htvshows'),
    path('hmovies/<int:hmovie_id>',views.hmovie, name='hmovie'),
    path('htvshows/<int:htvshow_id>',views.htvshow, name='htvshow'),
    path('htvshows/<int:htvshow_id>/like',views.htvshowLike, name='htvshowLike'),
    path('htvshows/Tform',views.Tform, name='Tform'),
    path('hmovies/Mform',views.Mform, name='Mform'),
    
]