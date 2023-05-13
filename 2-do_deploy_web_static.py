#!/usr/bin/python3
"""
Distributes an archive to web servers
"""

import os.path
from fabric.api import run, put, env

env.hosts = ["18.204.9.215", "54.144.45.169"]


def do_deploy(archive_path):
    """deploys archive to server"""

    # Checks is the file exists
    if os.path.isfile(archive_path) is False:
        return False

    # Finds the name of the file
    file = archive_path.split('/')[-1]
    name = file.split('.')[0]

    # Uploads archive to webserver
    if put(archive_path, '/tmp/{}'.format(file)).failed is True:
        return False
    
    # deletes archive destination is exists
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False

    # creates a new one
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False

    # Uncompress the archive to the folder
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
           .format(file, name)).failed is True:
        return False

    # Delete the archive from the web server
    if run('rm /tmp/{}'.format(file)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* \
           /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False

    # Delete the symbolic link current
    if run('rm -rf /data/web_static/current').failed is True:
        return False

    # Create a new symbolic link
    if run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
           format(name)).failed is True:
        return False

    # Success
    return True
