# uaa490-2023-10-16-airline

The usual setup:

git clone https://github.com/chezmarcbrown/uaa490-2023-10-16-airline.git
cd uaa490-2023...
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

mv db-2023-10-16.sqlite3 db.sqlite3 # gets you set with a few airports and flights
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

