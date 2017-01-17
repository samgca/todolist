
Deploy to Heroku

First create a heroku account

Then you need to install your Heroku toolbelt which you can find here (you can skip the installation if you've already installed it during setup): https://toolbelt.heroku.com/

Then authenticate your Heroku account on your computer by running this command:

heroku login

Pick an application name [project-name].herokuapp.com

We need to choose a name that nobody else has taken. The name can be anything you want, but Heroku is quite strict as to what characters you can use: you're only allowed to use simple lowercase letters (no capital letters or accents), numbers, and dashes (-).

heroku create [project-name]

If you can't think of a name, you can instead run

heroku create

and Heroku will pick an unused name for you.

If you ever feel like changing the name of your Heroku application, you can do so at any time with this command (replace the-new-name with the new name you want to use):

heroku apps:rename [new-project-name]

Create an empty git

git init (you can skip this if you've already create a repository)

Add the code to the repository

git add . -A

When you ran heroku create, it automatically added the Heroku remote for our app to our repository. Now we can do a simple git push to deploy our application:

Before we make a push we need to go to our Heroku account and add the Add-on Heroku Postgres. The go to the settings and click on the Reveal Config Vars buttons.
Create a new variable ON_HEROKU and set to True

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
