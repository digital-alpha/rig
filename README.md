# rig
Pipeline for unstructured data processing

# Setting up

### Follow these steps to setup the project locally
```
1.git clone https://github.com/rdamarapati/rig.git
2.cd rig
3.Set up a virtual environment
4.Install Postgresql
   a) create a database - "rig" 
5.pip install -r requirements.txt
  > Download and Unzip en_core_web_sm-2.0.0 from https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz
  > Run Pip install . inside the unziped folder 
6.Update .env config file with the DB_NAME, HOST,USERNAME and PASSWORD
7.python manage.py makemigrations
7.python manage.py migrate
8.python manage.py createsuperuser
9.python manage.py runserver
```

###Postgresql 
```
Start/Stop Server -  pg_ctl -D /usr/local/var/postgres start\stop 
```

After these steps the project should be up at [http://localhost:8000/](http://localhost:8000/)

Now you can access the Admin Panel through [http://localhost:8000/admin](http://localhost:8000/admin) and login with your newly created username and password.
