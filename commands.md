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

