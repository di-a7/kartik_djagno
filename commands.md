# install Virtual Environment
pip install virtualenv

# create virtual env
python -m venv env         # env is the name of virtualenv, env ko sattama aaru name you can define
or, 
virtualenv env             # env is userdefined, and be named anything

# activate virtual env
env\Scripts\activate (win)
source env/Scripts/activate (mac)
source env/bin/activate (linux)

# install django
pip install django

# to start django project
django-admin startproject project_name .        # '.' is optional

# run the server
python manage.py runserver

# create app
python manage.py startapp app_name

# create migration file
python manage.py makemigrations

# migrate to database
python manage.py migrate

# Python shell 
python manage.py shell

model_name.objects.all()      # all data in that model are displayed
model_name.objects.all().values()      # all data in that model are displayed with detail

# Create data
model_name.objects.create(title = "...", description= "....", status = "...", field1 = "...", ....)

# fetch single data from the model/table / Reterive data
a = model_name.objects.get(id = 1)
a.field1
a.field2

# save the updated data
a.field1 = "new data"
a.save()

# delete data
a.delete()

# filter data
model_name.objects.filter(field1 = "...", field2 = "...", ....)