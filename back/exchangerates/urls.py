from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    path('',views.get_rates),
    path('get/',views.calculate_rates)
]
