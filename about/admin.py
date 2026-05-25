from django.contrib import admin
from .models import AboutMe, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AboutMe)
class AboutMeAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
