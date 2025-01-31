from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('books/',books),
    path('returns/',returns),
    path('my_bag/',my_bag),
    path('readers/',readers),
    path('readers/add',save_reader),
]
