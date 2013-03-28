## SoCraTes Conference 
Site for [www.socrates-conference.de](http://www.socrates-conference.de) based on 
[Django](https://www.djangoproject.com/) and [Bootstrap](http://twitter.github.com/bootstrap/index.html).

## License

The MIT License (MIT)
Copyright (c) 2012 Benjamin Reitzammer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Installation

### For development

Note: Due to naming restrictions in python modules, the name of the directory that contains the git repo should not contain the dot-character
For Linux: run "apt-get install libpq-dev python-dev" beforehand to install the requirements

    # create a virtualenv & activate it
    
    $> pip install -r requirements_dev.txt
    
    # say no, when asked to create a superuser
    $> ./manage.py syncdb --migrate
    $> ./manage.py createsuperuser
    
    $> ./manage.py runserver

Due to unfortunate naming of this repo and the way Django works you should rename the directory your clone resides in to something without dots.  
TL;DR rename the directory of your local clone to socrates-conference


### Production Install

- Make sure the correct SITE_ID is set in settings.prod
- create a `settings/keys.py` file that contains values for the secret settings listed in 
  `settings/prod.py`
- set the environment variable "ENV_PROD" to some true value, e.g. 1
  
#### Heroku style

    $> heroku config:add ENV_PROD=1
    $> heroku config:add TWITTER_CONSUMER_KEY=xxxx
    $> heroku config:add TWITTER_CONSUMER_SECRET=xxxx
    $> heroku config:add SECRET_KEY=xxxx
    $> heroku config:add EMAIL_HOST_PASSWORD=xxxx
    
    # say no, when asked to create a superuser
    $> heroku run python manage.py syncdb --migrate
    $> heroku run python manage.py createsuperuser

    $> heroku ps:scale web=1  
