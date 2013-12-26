#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

#functie print bestand(f) en lees.
def print_all(f):
    print f.read()

# bestand(f) seek naar 0. Dus zoek line 0.
def rewind(f):
    f.seek(0)

# functie print een lijn var line count en bestand(f)
def print_a_line(line_count, f):
    print line_count, f.readline()

# variabele open het opgegeven bestand
current_file = open(input_file)

print "First let's print the whole file:\n"

# functie bestand en lees heel variabele
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
