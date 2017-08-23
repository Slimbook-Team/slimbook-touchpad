#! /usr/bin/python3
# -*- coding: utf-8 -*-

import shlex
import os.path
import subprocess


def run(comando):
    args = shlex.split(comando)
    p = subprocess.Popen(args, bufsize=10000, stdout=subprocess.PIPE)
    answer = p.communicate()[0].decode('utf-8')
    return answer

class Synclient(object):
    def __init__(self):
        self.properties = {}

    def read_synclient(self):
        properties = {}
        for element in run('synclient -l').split('\n'):
            if element.find('=')>-1:
                proper,value = element.split('=')
                proper = proper.strip()
                value = value.strip()
                properties[proper] = value
        self.properties = properties

    def get(self,key):
        self.read_synclient()
        if key in self.properties.keys():
            return self.properties[key]
        return None
