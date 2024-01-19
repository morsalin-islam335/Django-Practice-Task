from django import forms 

from musician.models import Musician
from album.models import Album  

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

