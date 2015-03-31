#!/bin/bash

from .settings import NODE_ENVIRONMENT_DIRECTORY, NODE_ACTIVATE_PATH, \
    NPM_ENV, ROOT

import subprocess
import os


class NodeEnv():
    def __init__(self):
        if not self.node_exist():
            self.install_node_environment()

    def node_exist(self):
        return os.path.isfile(NODE_ACTIVATE_PATH)

    def install_node_environment(self):
        cmd = ['nodeenv', '--prebuilt', NODE_ENVIRONMENT_DIRECTORY]
        p1 = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE)

        for line in p1.stdout:
            print line

        p1.wait()

        self.install_npm_requirements()

    def install_npm_requirements(self):
        print 'installing npm packages'
        cmd = [NPM_ENV, 'install']
        p3 = subprocess.Popen(cmd, cwd=ROOT,
                              stdout=subprocess.PIPE)
        for line in p3.stdout:
            print line
        p3.wait()


