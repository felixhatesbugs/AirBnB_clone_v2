#!/usr/bin/python3
"""Deletes out-of-date archives"""

import os
from fabric.api import lcd, cd, run, local, env

env.hosts = ["18.204.9.215", "54.144.45.169"]


def do_clean(number=0):
    """
    Deletes out of date archives
    """

    number = 1 if int(number) == 0 else int(number)

    archive = sorted(os.listdir("versions"))
    [archive.pop() for i in range(number)]

    with lcd("versions"):
        [local("rm ./{}".format(f)) for f in archive]

    with cd("/data/web_static/releases"):
        # lists files in reverse modification time
        archive = run("ls -tr").split()
        archive = [f for f in archive if "web_static_" in f]
        [archive.pop() for i in range(number)]
        [run("rm -rf ./{}".format(i)) for i in archive]
