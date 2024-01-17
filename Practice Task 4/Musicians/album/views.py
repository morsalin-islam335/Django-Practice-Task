from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse


from . models import Album, Musician
def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {"albums":albums})


from . forms import ADD_Album, ADD_Musician
def addMusician(request):
    if request.method == "POST":
        form = ADD_Musician(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ADD_Musician()
    return render(request, 'addMusician.html', {"form":form})


def addAlbum(request):
    if request.method == "POST":
        form = ADD_Album(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ADD_Album()
    return render(request, 'addAlbum.html',{"form":form})




from . forms import Edit_Musician

def editMusician(request, id):
    musician = Musician.objects.get(id = id)
    if request.method == "POST":
        form = Edit_Musician(request.POST, instance= musician)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = Edit_Musician(instance=musician)
        return render(request, 'addMusician.html', {"form": form})



def deleteMusician(request, id):
    Musician.objects.get(id = id).delete()
    return redirect("homepage")


from .forms import Edit_Album
def editAlbum(request, id):
    album = Album.objects.get(id = id)
    if request.method == "POST":
        form = Edit_Album(request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = Edit_Album(instance=album)
    return render(request, 'addAlbum.html',{"form":form})