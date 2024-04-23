from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album


# Create your views here.
def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = AlbumForm()
    return render(request, "albums/add_album.html", {"form": form})


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    print("🐍 File: albums/views.py | Line: 20 | edit_album ~ album", album)
    form = AlbumForm(instance=album)
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    return render(request, "albums/edit_album.html", {"form": form})


def delete_album(request, id):
    Album.objects.get(pk=id).delete()
    return redirect("homepage")
