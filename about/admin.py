from django.contrib import admin
from .models import AboutMe
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AboutMe)
class AboutMeAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


