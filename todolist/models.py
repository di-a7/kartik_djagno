from django.db import models

# Create your models here.
class Todo(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   status = models.BooleanField(default=False)
   
   def __str__(self):
      return f"{self.title} - {self.status}"


# Portfolio
# Profile(class name): (name, email, phone, contact, education, hobbies, skills)Fields of User class

# Education: degree, institution, year_of_passing, percentage

# projects :  title, description, techstack ,Link

# admin customization for Portfolio models
# frontend pages for portfolio 