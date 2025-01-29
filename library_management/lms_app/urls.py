from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('shop/',shopping),
    path('save/',save_student),
    
]
