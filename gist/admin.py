from django.contrib import admin
from .models import Gist

#customizing your admin area
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id','gist','gistDate')
    list_display_links = ('id','gist','gistDate') #clickable links
    list_filter = ('gistDate',)
    search_fields = ('gist',)
    list_per_page = 20 #pagination


# Register your models here.
admin.site.register(Gist)