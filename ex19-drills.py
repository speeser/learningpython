#!/usr/bin/python
#-*- coding: utf-8 -*-

def myfunction(arg1, arg2):
    print "Dit is mijn functie"
    print "%s en %s zijn al jaren samen" % (arg1, arg2)

naam =  raw_input("Wat is je naam? ")
naamvrouw = raw_input ("Wat is de naam van je vrouw? ")
myfunction(naam, naamvrouw)
