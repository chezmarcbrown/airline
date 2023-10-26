import csv
from flights.models import Airport

AIRPORTS_FILENAME = "flights/seeddata/airports.csv"
def run():
    print(f'Opening file: {AIRPORTS_FILENAME}')
    with open(AIRPORTS_FILENAME) as incsvfile:
        reader = csv.DictReader(incsvfile)
        for row in reader:
            print(f'Processing row: {row}')
            code = row['code']
            city = row['city']
            # if not Airport.objects.exists(code=code, city=city):
            #     a=Airport(code=code, city=city)
            #     a.save()
            Airport.objects.get_or_create(code=code, city=city)