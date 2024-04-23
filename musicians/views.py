from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician


# Create your views here.
def add_musician(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MusicianForm()
    return render(request, "musicians/add_musician.html", {"form": form})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    form = MusicianForm(instance=musician)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    return render(request, "musicians/add_musician.html", {"form": form})
