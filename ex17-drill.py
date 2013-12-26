#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

idata = open(from_file, 'r').read()

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w').write(idata)

print "Het bestand is %d bytes groot" % len(idata)
