#!/usr/bin/python
#-*- coding: utf-8 -*-

def plus(x, y):
    print "We tellen x en y bij elkaar op: %d + %do =" % (x, y)
    return x + y

optelsom = plus(55, 10)

print "%d" % optelsom

def min(a, b):
    print "We trekken a en b van elkaar af: %d - %d =" % (a, b)
    return a - b

aftrekken = min(35, 40)

print "%d" % aftrekken


