#!/usr/bin/python
# -*- coding: utf-8 -*-

def my_func(numb, plus):
    i = 0
    numbers = []
    for i in range(0, 6):
        print "At the top i is %d" % i
        numbers.append(i)

        #i = range(0,6)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "the numbers: "

my_func(20, 3)


# for num in numbers:
#    print num
