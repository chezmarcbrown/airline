import csv, os
from slugify import slugify

from movies.models import Movie
from tempfile import NamedTemporaryFile
from django.core.files import File

DIR = "movies/seeddata/"
FILENAME = os.path.join(DIR, 'top-movies.csv')

def run():

    print(f'Reading file: {FILENAME}')
    with open(FILENAME) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'\t{row["title"]}', end="... ")
            title = row["title"]
            year = int(row["year"])
            rating = float(row["rating"])
            director = row["director"]
            plot = row["plot"]
            url = row["url"]
            if Movie.objects.filter(         
                movie_title=title, release_year=year).exists():
                print(f'already in database.')
            else:
                m = Movie(movie_title=title, release_year=year, director=director, movie_plot=plot, rating=rating)
                m.save()
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(open(os.path.join(DIR,url), 'rb').read())
                img_temp.flush()
                #m.movie_poster.save(f"image_{m.pk}", File(img_temp))
                m.movie_poster.save(f"{slugify(title)}-{year}.jpg", File(img_temp))
                print(f'added to database.')

	