from fabric.api import local, run, env

env.hosts = ["localhost"]

def production():
    env.hosts = ["www.ariel17.com.ar", ]

def hola():
    print "hola!"

def touch():
    local("touch /tmp/ariel")

def remote_pull():
    run("cd www")
    run("git pull")
