#!/usr/bin/python
# -*- coding: utf-8 -*-

class User():
    tt = """
class {0}():
    nesto da napisem
    """
    def __init__(self, name):
        self.name = name

    def generate(self):
        print self.tt.format(self.name)
