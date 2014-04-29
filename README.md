## SoCraTes Conference 
Site for [www.socrates-conference.de](http://www.socrates-conference.de) based on 
[Django](https://www.djangoproject.com/) and [Bootstrap](http://getbootstrap.com/).

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
    $> export SECRET_KEY=somesecret
    $> export DEBUG=True
    $> ./manage.py runserver
    
Now the development server is running and reachable at localhost:8000 

### Initial Deploy to Heroku

    $> heroku config:add SECRET_KEY=somereallylongsecretrandomstring
    $> heroku ps:scale web=1  

## License

The MIT License (MIT)
Copyright (c) 2012 Benjamin Reitzammer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

