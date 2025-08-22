from django.shortcuts import render
from django.conf import settings 

# Create your views here.

def about(request):
    return render(request, 'home/about.html')
def home(request):
    restaurant_name = settings.RESTAURANT_NAME 
    return render(request,'home/: index.html' {'restaurant_name': restaurant_name})
