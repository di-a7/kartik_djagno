from django.urls import path
from .views import *   # import all function from views
# from . import views       # import view file from this directory
urlpatterns = [
   path('first/', first),
   path('home/', home),
   path('contact/', contact),
   path('tasks/', task),
   path('tasks/create/', task_create),
]

