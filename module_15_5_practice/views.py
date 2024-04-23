from django.shortcuts import render
from albums.models import Album


def home(request):
    albums = Album.objects.all()
    return render(request, "home.html", {"albums": albums})
