from django.contrib import admin
from .models import contact,VideoClips,VideoClips1,VideoClips2,VideoClips3
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','date')
    list_display_links = ('id','fullname','date')
    list_filter = ('id','fullname','date',)
    search_fields = ('fullname',)
    list_per_page = 20 #pagination

class VideoClipsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    list_display_links = ('id','name',)
    list_filter = ('id','name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class VideoClips1Admin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    list_display_links = ('id','name',)
    list_filter = ('id','name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class VideoClips2Admin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    list_display_links = ('id','name',)
    list_filter = ('id','name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class VideoClips3Admin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    list_display_links = ('id','name',)
    list_filter = ('id','name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

admin.site.register(contact, contactAdmin)
admin.site.register(VideoClips, VideoClipsAdmin)
admin.site.register(VideoClips1, VideoClips1Admin)
admin.site.register(VideoClips2, VideoClips2Admin)
admin.site.register(VideoClips3, VideoClips3Admin)

