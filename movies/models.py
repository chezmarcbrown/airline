from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.core.exceptions import ValidationError

# Create your models here.
def validate_rating(value):
	print(f'calling validate rating {value}')
	if value < 0.0:
		raise ValidationError(f'Rating must be at least 0.0')
	elif value > 10.0:
		raise ValidationError(f'Rating cannot exceed 10.0')


class Movie(models.Model):
	movie_title = models.CharField(max_length=150)
	release_year = models.IntegerField()
	director = models.CharField(max_length=100)
	movie_poster = models.ImageField(upload_to='images/', blank=True)
	movie_plot = models.TextField()
	rating = models.FloatField(default=0.0, validators=[validate_rating])
	
	def __str__(self):
		return self.movie_title


