#!/usr/bin/python3
"""Creates and distribute archive to a web server."""

import os.path
from datetime import datetime
from fabric.api import local, run, put, env


env.hosts = ["18.204.9.215", "54.144.45.169"]


def do_pack():
    """
    creates an archive file
    and stores it in the versions
    folder
    """

    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                         date.month,
                                                         date.day,
                                                         date.hour,
                                                         date.minute,
                                                         date.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


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

    if run("rm -rf /data/web_static/releases/{}/web_static"
           .format(name)).failed is True:
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


def deploy():
    """creates and distributes archive to server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
