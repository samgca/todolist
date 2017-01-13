
Develop a django project with heroku

First commit create a django project with a testapp. The testapp display the text 'Django Workshop'

Second commit Make changes to upload in heroku

But first, Heroku needs us to install a few new packages

pip install dj-database-url gunicorn whitenoise

After the installation is finished, go to the directory django_heroku and run this command:

pip freeze > requirements.txt

Open requirements.txt and add the following line at the bottom:

psycopg2==2.6.1

Procfile

Procfile tells Heroku which commands to run in order to start our website. Create a file called Procfile in django_project directory and add this line:

web: gunicorn django_project.wsgi --log-file -

This line means that we're going to be deploying a web application, and we'll do that by running the command gunicorn django_project.wsgi. Save it.

The runtime.txt file

We also need to tell Heroku which Python version we want to use. This is done by creating a runtime.txt in the django_project directory using your editor's "new file" command, and putting the following text inside:

python-3.6.0

https://devcenter.heroku.com/articles/python-runtimes

settings.py

Heroku wants to use Postgres while we use SQLite for example. That's why we need to create a separate file for settings that will only be available for our local environment.

Go ahead and create django_project/production_settings.py file. It should contain your DATABASE setup file. Just like that:

import dj_database_url
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

For some setups, most notably Heroku, you should use SECURE PROXY SSL HEADER:

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

wsgi.py

Open the django_project/wsgi.py file and add these lines:

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)

Static and Media Files

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

Heroku account

You need to install your Heroku toolbelt which you can find here (you can skip the installation if you've already installed it during setup): https://toolbelt.heroku.com/

Then authenticate your Heroku account on your computer by running this command:

heroku login

Pick an application name [project-name].herokuapp.com

We need to choose a name that nobody else has taken. The name can be anything you want, but Heroku is quite strict as to what characters you can use: you're only allowed to use simple lowercase letters (no capital letters or accents), numbers, and dashes (-).

heroku create django-with-heroku

If you can't think of a name, you can instead run

heroku create

and Heroku will pick an unused name for you.

If you ever feel like changing the name of your Heroku application, you can do so at any time with this command (replace the-new-name with the new name you want to use):

heroku apps:rename the-new-name

If you want to use a git repository:

git remote add heroku git@heroku.com:django-with-heroku.git

Deploy to Heroku!

When you ran heroku create, it automatically added the Heroku remote for our app to our repository. Now we can do a simple git push to deploy our application:

git push heroku master

Visit your application

You’ve deployed your code to Heroku, and specified the process types in a Procfile (we chose a web process type earlier). We can now tell Heroku to start this web process.

To do that, run the following command:

heroku ps:scale web=1

This tells Heroku to run just one instance of our web process. Since our blog application is quite simple, we don't need too much power and so it's fine to run just one process. It's possible to ask Heroku to run more processes (by the way, Heroku calls these processes "Dynos" so don't be surprised if you see this term) but it will no longer be free.

We can now visit the app in our browser with heroku open.

heroku open

Ia an error occur run the following command:

heroku logs -t

If the error is from database run

heroku run python manage.py migrate

You need to create a new user

heroku run python manage.py createsuperuser

The command prompt will ask you to choose a username and a password again.
