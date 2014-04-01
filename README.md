## SoCraTes Conference 
Site for [www.socrates-conference.de](http://www.socrates-conference.de) based on 
[Django](https://www.djangoproject.com/) and [Bootstrap](http://getbootstrap.com/).

## License

The MIT License (MIT)
Copyright (c) 2012 Benjamin Reitzammer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Installation

### Requirements

* Python, >=v2.6 ... not v3.x 
* Under Linux: run "apt-get install libpq-dev python-dev" beforehand to install the requirements
* [pip](http://www.pip-installer.org/) ... easiest to install via [get-pip.py](http://www.pip-installer.org/en/latest/installing.html#install-or-upgrade-pip)
* [virtualenv](http://www.virtualenv.org/) ... easiest to install [globally via pip](http://www.virtualenv.org/en/latest/#installation)
* Optional: Consider using [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) to make handling virtualenvs easier. 

### Prepare for development

**NOTE:** Due to unfortunate naming of this repo and the way Django/Python works you should rename the directory your clone resides in to something without dots.  
TL;DR rename the directory of your local clone to socrates-conference

    # create a virtualenv & activate it ... sth like `virtualenv socratesconf && . socratesconf/bin/activate`
    
    $> pip install -r requirements.txt
    $> ./manage.py syncdb --migrate
    $> ./manage.py runserver
    
Now the development server is running and reachable at localhost:8000 

### Production Install

- Make sure the correct SITE_ID is set in settings.prod
- create a `settings/keys.py` file that contains values for the secret settings listed in 
  `settings/prod.py`
- set the environment variable "ENV_PROD" to some true value, e.g. 1
  
#### Heroku style

    $> heroku config:add ENV_PROD=1
    $> heroku config:add SECRET_KEY=xxxx
    $> heroku run python manage.py syncdb --migrate
    $> heroku ps:scale web=1  
