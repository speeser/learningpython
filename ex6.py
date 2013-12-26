# x is een variable met de inhoud van een string + een getal
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# y is een variable met de inhoud van een string + 2 strings variablen
y = "Those who know %s and those who know %s." % (binary, do_not)

print x
print y

# %r print heel x (string + getal) raw inhoud
print "I said: %r." % x
# %s print heel y (+ 2 strings)
print "I also said: '%s'." % y

#Hilarious is alleen True or False, in dit geval False
hilarious = False
# print de string raw %r.
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# string + string = zin
print w + e
