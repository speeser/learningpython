#!/usr/bin/python
#-*- coding: utf-8 -*-

# Import argv module
from sys import argv

# Geef argument filename 
script, filename = argv

# txt is een variable en opent argument filename
txt = open(filename)

# print de filename opgeven argument
print "Here's your file %r:" % filename

# print variable in dit geval filename opgegeven en lees
print txt.read()

# laat een input geven in dit geval een filenaam
print "Type the filename again:"
file_again = raw_input("> ")

# maak een variable aan en open filenaam
txt_again = open(file_again)

# uitvoeren van het uitlezen van het bestand.
print txt_again.read()
