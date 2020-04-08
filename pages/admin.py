from django.contrib import admin
from .models import contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','date')
    list_display_links = ('id','fullname','date')
    list_filter = ('id','fullname','date',)
    search_fields = ('fullname',)
    list_per_page = 20 #pagination

admin.site.register(contact, contactAdmin)
