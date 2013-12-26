#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "Opening the file..."
target = open(filename, 'w')

print "Now I'm going to ask tou for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Now I'm going to write these to the file."

target.write('{0}\n{1}\n{2}\n'.format(line1, line2, line3))

print "And finally, we close it."
target.close()
