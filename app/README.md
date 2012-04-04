# Installing

    # create a virtualenv & activate it
    # install requirements sth like 'pip install -r requirements.txt'
    ./manage.py syncdb  (and say no when prompted to create a superuser)
    ./manage.py migrate gatekeeper
    ./manage.py createsuperuser