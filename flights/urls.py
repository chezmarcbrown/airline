from . import views
from django.urls import path

app_name = "flights"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flight_id>', views.flight, name="flight")
]