from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
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

def contact(request):
   context = {
      "title" : "Contact",
      "first_line": "Contact Page",
      "second_line":"This is a contact page rendering from contact function"
   }
   return render(request,'contact.html',context)

def task(request):
   tasks = Todo.objects.all()
   total = tasks.count()
   complete = len(Todo.objects.filter(status = True))
   print(complete)
   incomplete = Todo.objects.filter(status = False).count()
   context = {
      "tasks" : tasks,
      "total_tasks": total,
      "complete_tasks": complete,
      "incomplete_tasks": incomplete,
   }
   return render(request,'tasks.html', context)

def task_create(request):
   if request.method == "POST":
      title1 = request.POST.get('title')
      description1 = request.POST.get('description')
      if title1 == "" or description1 == "":
         context = {
            "error":"Both fields are required."
         }
         return render(request, 'create.html', context)
      Todo.objects.create(title = title1, description = description1)
      return redirect('/tasks/')
   
   return render(request,'create.html')
