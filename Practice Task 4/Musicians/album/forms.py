# Add Musician
from django import forms

from . models import Musician, Album

class ADD_Musician(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class Edit_Musician(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'


class ADD_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'



class Edit_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'



