from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('profile/<str:username>', views.profile_list, name='profile'),
    path('recommend/',views.recommend),
]
