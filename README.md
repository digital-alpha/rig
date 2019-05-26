# rig
Pipeline for unstructured data processing

# Setting up

### Follow these steps to setup the project locally
```
git clone https://github.com/rdamarapati/rig.git
cd rig
Set up a virtual environment
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

After these steps the project should be up at [http://localhost:8000/](http://localhost:8000/)

Now you can access the Admin Panel through [http://localhost:8000/admin](http://localhost:8000/admin) and login with your newly created username and password.