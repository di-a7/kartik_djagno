from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
   return HttpResponse("<h1>Welcome</h1>")

def home(request):
   user = [
      {"name": "Aarav", "age": 15, "address": "Kathmandu"},
      {"name": "Sita", "age": 23, "address": "Bhaktapur"},
      {"name": "Ramesh", "age": 30, "address": "Lalitpur"},
      {"name": "Aarav", "age": 25, "address": "Kathmandu"}, 
      {"name": "Mina", "age": 28, "address": "Pokhara"},
      {"name": "Sita", "age": 23, "address": "Bhaktapur"},
      {"name": "Kiran", "age": 50, "address": "Butwal"},
      {"name": "Kiran", "age": 35, "address": "Butwal"},
      {"name": "Kiran", "age": 35, "address": "Butwal"},
      {"name": "Kiran", "age": 65, "address": "Butwal"},
      {"name": "Nisha", "age": 12, "address": "Dharan"},
      {"name": "Ramesh", "age": 30, "address": "Lalitpur"},
      {"name": "Anil", "age": 57, "address": "Biratnagar"},
   ]

   a = "Welcome to the page"
   context = {
      "title":"Homepage",
      "first_line": a,
      "second_line": "This is a home page. rendering from home function",
      "people" : user
   }
   return render(request,'home.html', context)


# create function home, about_us, contact
# create respective url(home,about_us,contact)

# url -> views