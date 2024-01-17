# Django Rest API
This project uses the <a href="https://www.django-rest-framework.org/">Django Rest Framework</a> to build an api.

## Install
1. Create a folder
``` bash
mkdir DjangoREST
```
2. cd into the folder and create a virtual environment
``` bash
python -m venv virt
```
3. Activate the virtual environment
``` bash
source virt/Scripts/activate
```
4. Git Clone
``` bash
git clone 
```
5. Install django and django_rest_framework
``` bash
pip install -r requirements.txt
```
6. Create database migrations
``` bash
python manage.py makemigrations
```
7. Make migrations
``` bash
python manage.py migrate
```
8. Run the api
``` bash
python manage.py runserver
```

## Endpoints
1. http://localhost/api/users - GET Users
2. http://localhost/api/message - GET messages
3. http://localhost/api/message-create - POST messages
4. http://localhost/api/groups - GET groups