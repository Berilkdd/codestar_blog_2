from django.shortcuts import render
from .models import AboutMe

# Create your views here.

def about_me(request):
    
    about = AboutMe.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
