from django.urls import path
from .views import *

urlpatterns = [
    path('about/',views.about, name='about'),
    path('',views.home, name='home'),
    
]