from fabric.api import local, env

def production():
    env['epioapp'] = 'scrts-conf-prod'

def staging():
    env['epioapp'] = 'scrts-conf-stage'

def epio(commandstring):
    local("epio {0} -a {1}".format(
        commandstring,
        env['epioapp']))

def deploy():
    """ An example deploy workflow """
    local("./manage.py collectstatic")
    epio('upload')