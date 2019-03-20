# BLOG-API

This is a  rest api  that is made with Django Rest Framework that exposes articles and categories for a blog. It has the following functionality:

1. Admin user - create using command line
* log in(Class-based API views)
* create, view, edit, delete article(Viewset Classes)
* create, view, edit, delete category(Viewset Classes)

2. Category - name

3. Article - writer (foreign key), title, content, category (foreign key), image

4. Permissions:
* only admin can create, edit, and delete articles and categories
* no login required for viewing articles


Technologies used
Django: The web framework for perfectionists with deadlines (Django builds better web apps with less code).
DRF: A powerful and flexible toolkit for building Web APIs
Installation
If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python here.

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

$ git clone https://github.com/EUGINELETHAL/BLOG-API

Dependencies
Cd into your the cloned repo as such:
    $ cd BLOG-API

Create and fire up your virtual environment:
    $ virtualenv  venv -p python3
    $ source venv/bin/activate

Install the dependencies needed to run the app:
    $ pip install -r requirements.txt

Make those migrations work
    $ python manage.py makemigrations
    $ python manage.py migrate
Run It

Fire up the server using this one simple command:
  $ python manage.py runserver

You can now access the file api service on your browser by using
   http://localhost:8000/api/v1
