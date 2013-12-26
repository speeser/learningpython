#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "Hit Enter..."
raw_input("?")

print "We gaan %r lezen" % filename
print "Open het bestand..."
bestand = open(filename, 'r')

print "cat %r" % filename
print bestand.read()

print "sluit het bestand"
bestand.close()

