#!/usr/bin/python3
"""
Generates a .tgz archive
from the contents of the web_static folder
"""

import os.path as path
from datetime import datetime
from fabric.api import local


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

    if path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
