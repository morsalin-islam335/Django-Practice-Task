from django.shortcuts import render

from django.http import HttpResponse

from . forms import User


def saveFileFromForm(file):
    with open("files/uploads/"+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def FormAPI_RENDER(request):
    # return render(request, 'user.html', {"user": User})
    if request.method == "POST":
        form = User(request.POST, request.FILES) # we use request.FILES for  take files input

        if form.is_valid():
            print(form.cleaned_data)
            # print('duration type', type(form.cleaned_data['duration']), 'duration: ', form.cleaned_data.get('duration'))
            password  = form.cleaned_data['password']
            # file = form.cleaned_data['file']
            # print("file name with extension", file.name)
            # saveFileFromForm(file)
            # context = form
            return render(request, 'form_API_Data_Page.html', {"form":form, 'password': password})
    else:
        form = User()
    return render(request, 'user.html', {"user": form})





from .forms import ModelForm1
def DummyForm(request):
    if request.method == "POST":
        form = ModelForm1(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'homepage.html')
    else:
        form = ModelForm1()
    return render(request, 'model1.html', {"form": form})






