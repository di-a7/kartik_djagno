from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
   return HttpResponse("<h1>Welcome</h1>")

# create function home, about_us, contact
# create respective url(home,about_us,contact)