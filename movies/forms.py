from django import forms
from .models import Movie 


# Create your forms here.
class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('movie_title', 'release_year', 'rating', 'director', 'movie_poster', 'movie_plot')
