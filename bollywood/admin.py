from django.contrib import admin
from .models import Movies,Tvshows,gist,tvshowgist,Like,Dislike,MovieLike,MovieDislike
#customizing your admin area
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')
    list_display_links = ('id','name') #clickable links
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class TvshowsAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')
    list_display_links = ('id','name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class gistAdmin(admin.ModelAdmin):
    list_display = ('id','gists','date',)
    list_display_links = ('id','gists','date',)
    list_filter = ('gists',)
    search_fields = ('gists',)
    list_per_page = 20 #pagination

class tvshowgistAdmin(admin.ModelAdmin):
    list_display = ('id','gists','date')
    list_display_links = ('id','gists','date')
    list_filter = ('gists',)
    search_fields = ('gists',)
    list_per_page = 20 #pagination

class LikeAdmin(admin.ModelAdmin):
    list_display = ('id','tvshow','date')
    list_display_links = ('id','tvshow','date')
    list_filter = ('tvshow',)
    search_fields = ('tvshow',)
    list_per_page = 20 #pagination

class DislikeAdmin(admin.ModelAdmin):
    list_display = ('id','tvshow','date')
    list_display_links = ('id','tvshow','date')
    list_filter = ('tvshow',)
    search_fields = ('tvshow',)
    list_per_page = 20 #pagination

class MovieLikeAdmin(admin.ModelAdmin):
    list_display = ('id','movie','date')
    list_display_links = ('id','movie','date')
    list_filter = ('movie',)
    search_fields = ('movie',)
    list_per_page = 20 #pagination

class MovieDislikeAdmin(admin.ModelAdmin):
    list_display = ('id','movie','date')
    list_display_links = ('id','movie','date')
    list_filter = ('movie',)
    search_fields = ('movie',)
    list_per_page = 20 #pagination

# Register your models here.
admin.site.register(Movies,MoviesAdmin)
admin.site.register(Tvshows,TvshowsAdmin)
admin.site.register(gist,gistAdmin)
admin.site.register(tvshowgist,tvshowgistAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Dislike,DislikeAdmin)
admin.site.register(MovieLike,MovieLikeAdmin)
admin.site.register(MovieDislike,MovieDislikeAdmin)



