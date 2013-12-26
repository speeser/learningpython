#-*- coding: utf-8 -*- 
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depening on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "Study drills:"
print "print this %r no matter what" % name

# Convert inches to centimeters
one_inche = 2.54
one_pound = 0.45359237
print "How many centimeters is 7 inche?", 7 * one_inche
print "How many kilo's are 9 pounds?", round(9 * one_pound)
