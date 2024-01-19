from django.shortcuts import render, redirect

# Create your views here.

from . forms import SignUpForm, UpdateProfile

from django.contrib import messages


from album.models import Album

def home(request):

    albums = Album.objects.all()
    return render(request, 'home.html', {"albums":albums})

    
def signUp(request):
    if request.user.is_authenticated:
        return redirect("profile") # authenticated user sign-up korta parba na.
    else:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Congratulations! Account Create Successfully.')
                return redirect('login')
        else:
            form = SignUpForm()
        return render(request, 'signUp.html', {"form":form})


from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout



from django.contrib import messages

def userLogin(request):
    if request.user.is_authenticated:
        return redirect("profile") # ek bar log in korla ar korar proiojon nai.
    else:

        if request.method == "POST":
            form = AuthenticationForm(request = request, data = request.POST)

            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']

                user = authenticate(username = user_name, password = user_password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully!")
                    
                    return redirect("profile")
                else:
                    
                    messages.warning(request, "log in information is incorrect")

        else:
            form  = AuthenticationForm()
        return render(request, 'login.html', {"form":form})

def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, 'profile.html')


def UserLogout(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect("homepage")

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash    
def changePasswordWitOldPassword(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if  request.method == "POST":
        form = PasswordChangeForm(user = request.user, data = request.POST) # eta keyword parameter  hisaba nay

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user) # er vitor a just parametter dila kaj hoia jay
            messages.success(request, 'Password Update Successfully.')
            return redirect("homepage")
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request,'passwdChange.html', {"form":form})


from django.contrib.auth.forms import SetPasswordForm

def changePasswordWithoutOldPassword(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = SetPasswordForm(user = request.user, data = request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request, 'Password Update Successfully.')
            return redirect("profile")

    else:
        form = SetPasswordForm(request.user)
    return render(request, "passwdChange.html", {"form":form})


def updateProfile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == 'POST':
        form =  UpdateProfile(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Successfully.')
            return redirect("homepage")
    else:
        form = UpdateProfile(instance = request.user)
    return render(request, 'updateProfile.html', {"form":form})


from project.forms import AlbumForm, MusicianForm



def addMusician(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form =MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = MusicianForm()
    return render(request, 'addMusicianForm.html', {"form":form})


from musician.models import Musician

def editMusician(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    musician = Musician.objects.get(id = id)

    if request.method == "POST":
        form =MusicianForm(request.POST, instance = musician)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = MusicianForm(instance = musician)
    return render(request, 'editMusicianForm.html', {"form":form})

def deleteMusician(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    Musician.objects.get(id = id).delete()
    return redirect("homepage")


def addAlbum(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form =AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = AlbumForm()
    return render(request, 'addAlbumForm.html', {"form":form})

from album.models import Album

def editAlbum(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    album = Album.objects.get(id = id) # ja album ta edit korta chai ta dhorta hoiba

    if request.method == "POST":
        form =AlbumForm(request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = AlbumForm(instance=album)
    return render(request, 'editAlbumForm.html', {"form":form})

def deleteAlbum(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    Musician.objects.get(id = id).delete()
    return redirect("homepage")
