from django.contrib import admin
from .models import Movies,Tvshows,gist,tvshowgist

#customizing your admin area
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id','name','date','like_counts','dislike_counts')
    list_display_links = ('id','name') #clickable links
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class TvshowsAdmin(admin.ModelAdmin):
    list_display = ('id','name','date','like_counts','dislike_counts')
    list_display_links = ('id','name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class gistAdmin(admin.ModelAdmin):
    list_display = ('id','gists','date','gist_like_counts','gist_dislike_counts')
    list_display_links = ('id','gists','date','gist_like_counts','gist_dislike_counts')
    list_filter = ('gists',)
    search_fields = ('gists',)
    list_per_page = 20 #pagination

class tvshowgistAdmin(admin.ModelAdmin):
    list_display = ('id','gists','date','gist_like_counts','gist_dislike_counts')
    list_display_links = ('id','gists','date','gist_like_counts','gist_dislike_counts')
    list_filter = ('gists',)
    search_fields = ('gists',)
    list_per_page = 20 #pagination
    
# Register your models here.
admin.site.register(Movies,MoviesAdmin)
admin.site.register(Tvshows,TvshowsAdmin)
admin.site.register(gist,gistAdmin)
admin.site.register(tvshowgist,tvshowgistAdmin)
