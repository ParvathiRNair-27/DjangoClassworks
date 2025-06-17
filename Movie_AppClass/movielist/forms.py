
# form structure

from django import forms
from movielist.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        # fields="__all__"
        fields=['movie_name','description','director_name','year','language','image']
