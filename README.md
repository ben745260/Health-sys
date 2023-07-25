# Health-sys
Install django 
>$pip install Django

Run pipenv
>$pipenv shell

Install python pip requiement list
>$pip install -r requirements.txt 

Run the server
>$python manage.py runserver

If you are not using Postgresql, change setting.py database part to:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
