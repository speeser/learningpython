#!/usr/bin/python
#-*- coding: utf-8 -*-

import os, sys, time, urllib2 # modules os om linux commando's uit te voeren, sys buildin, time voor sleep, urllib2 om http pagina's te fetchen.
import html2text # sudo easy_install html2text, dit is een html naar text parser
import pydoc # importeert pydoc om de pager te gebruiken (linux less)

def print_keywords():
    print "Python keywords."
    print "----------------"
    print "1. Een voorbeeld met de 'and' operator."
    print "2. Een voorbeeld met het del statement"
    print "3. Wat doet het 'from' statement / html2text parser / variable door pydoc pager (less)"
    print "4. Een voorbeeld van het not statement." 
    print "5. Een voorbeeld van het while statement." 
    print "6. Een voorbeeld van het with-as statement, dit is onderdeel van het with statement." 
    print "7. Een voorbeeld van het if, elif en else statement." 
    print "8. Een voorbeeld van het global statement." 
    print "9. Een voorbeeld van het or statement." 
    print "10. Een voorbeeld van het assert statement. (Error handling)" 
    print "11. Een voorbeeld van het pass keyword. Dit kun je gebruiken bij iets wat nog niet nodig is dus een functie die overgeslagen moet worden."
    print "12. Een voorbeeld van yield. Nog te moeilijk."
    print "13. Een voorbeeld van break."
    print "14. Een voorbeeld van except statement. (Error handling)"
    print "15. Een voorbeeld van een class. Nog te moeilijk."
    print "16. Een voorbeeld van het exec statement."
    print "17. Het verschil tussen for loop en while loop."
    print "18. Een voorbeeld van het raise statement."
    print "19. Een voorbeeld van het continue statement."
    print "20. Een voorbeeld van het finally statement."
    print "21. Een voorbeeld van het 'is' statement."
    print "22. Een voorbeeld van het 'return' statement."
    print "23. Een voorbeeld van een lambda functie."
    print "24. Data types uitgeschreven."
    print "25. String escape sequences uitgeschreven."

def start():
    print "Maak je keuze 1-25 of type exit: "
    keuze = raw_input("> ")
    if keuze == '1':
        and_operator()
    elif keuze == '2':
        if keuze == '2':
            del_statement()
    elif keuze == '3':
        if keuze == '3':
            from_statement()
    elif keuze == '4':
        if keuze == '4':
            not_statement()
    elif keuze == '5':
        if keuze == '5':
            while_statement()
    elif keuze == '6':
        if keuze == '6':
            with_as_statement()
    elif keuze == '7':
        if keuze == '7':
            elif_statement()
    elif keuze == '8':
        if keuze == '8':
            global_statement()
    elif keuze == '9':
        if keuze == '9':
            or_statement()
    elif keuze == '10':
        if keuze == '10':
            assert_statement()
    elif keuze == '11':
        if keuze == '11':
            pass_keyword()
    elif keuze == '12':
        if keuze == '12':
            yield_keyword()
    elif keuze == '13':
        if keuze == '13':
            break_statement()
    elif keuze == '14':
        if keuze == '14':
            except_statement()
    elif keuze == '15':
        if keuze == '15':
            class_statement()
    elif keuze == '16':
        if keuze == '16':
            exec_statement()
    elif keuze == '17':
        if keuze == '17':
            diff_between_for_while()
    elif keuze == '18':
        if keuze == '18':
            raise_statement()
    elif keuze == '19':
        if keuze == '19':
            continue_statement()
    elif keuze == '20':
        if keuze == '20':
            finally_statement()
    elif keuze == '21':
        if keuze == '21':
            is_statement()
    elif keuze == '22':
        if keuze == '22':
            return_statement()
    elif keuze == '23':
        if keuze == '23':
            lambda_function()
    elif keuze == '24':
        if keuze == '24':
            datatypes_func()
    elif keuze == '25':
        if keuze == '25':
            string_esc_func()
    elif keuze == 'exit':
        exit(0)
    else:
        start()

def and_operator():
    print "Geef het goede nummer tussen 1 en 5."
    num = raw_input("> ")
    num = int(num)
    if num < 5 and num > 2 and num is not 4:
        print "Je hebt het goede getal gevonden!"
        print "if num < 5 and num > 2 and num is not 4"
        print_keywords()
        start()
    else:
        print "Fout! Zoek het goede getal tussen 1 en 5."
        and_operator()

def del_statement():
    os.system('clear') # clear screen met de import os module 
    print "Dit is het del statement"
    print "------------------------"
    print ""
    print "Met het del statement kun je items uit een list halen."
    print ""
    a = [1, 2, 3, 4, 5, 6]
    b = ['one', 'two', 'three', 'four', 'five', 'six']
    c = ['bear', 'sheep', 'cat', 'dog']
    print "Hieronder 3 lists."
    print a
    print b
    print c
    del a[2]
    print ""
    print "Met 'del a[2]' is de nummer 3 uit de list weg:"
    print a
    print ""
    del b[0:3]
    print "Met del b[0:3] zijn de strings one, two, three uit de list b:"
    print b
    print ""
    del c[3]
    print "Met del c[3] is dog weg uit list c:"
    print c
    print ""
    print ""
    print_keywords()
    start()

def from_statement():
    os.system('clear')
    print "Het 'from' statement importeert een module."
    print ""
    print "Nadat je op enter hebt gedrukt vind je een html fetch van een pagina wat uitlegt wat import en from doet."
    print ""
    print "Bron: http://effbot.org/zone/import-confusion.htm"
    print ""
    print "In deze functie staan technieken om html om te zetten naar plaintext en ook om de plaintext door een pager te halen (pydoc)."
    raw_input(">Hit enter to continue...") # hit enter to continue
    print ""
    print ""
    print ""
    print ""
    print ""
    print ""
    html_fetch = urllib2.urlopen('http://effbot.org/zone/import-confusion.htm') # module urllib2 haalt http pagina's op.
    # print http_fetch.info() # info() haalt de html headers op.
    raw_html = html_fetch.read() # read leest plain text. zoals in een normaal bestand, maar dan de rauwe html.
    plain_text = html2text.html2text(raw_html) #html2text parser zet de html om naar plain text.
    pydoc.pager(plain_text)
    html_fetch.close()
    raw_input(">Hit enter to continue...") # hit enter to continue
    os.system('clear')
    print_keywords()
    start()

def not_statement():
    print "Geef 2 gelijke nummers op."
    num_1 = int(raw_input("Geef het eerste nummer> "))
    num_2 = int(raw_input("Geef het tweede nummer> "))
    if not (num_1 != num_2):
        print "Je hebt 2 gelijke nummers opgegeven!"
        print "if not (num_1 != num_2):"
        print_keywords()
        start()
    else:
        print "Fout! ."
        not_statement()
    os.system('clear')
    raw_input(">Hit enter to continue...") # hit enter to continue

def while_statement():
    os.system('clear')
    count = 0
    while (count < 9):
        count += 1
        print "Het getal %d in deze loop is kleiner dan: 9." % count

    print "Het getal is gelijk aan of grotere dan 9. De loop stopt."
    print raw_input(">Hit de enter toets...")
    print_keywords()
    start()

def with_as_statement():
    os.system('clear')
    os.system('ls -l')
    bestand = raw_input("Kies een bestandsnaam: ")
    with open(bestand) as f:
        for line in f:
            print '    ' + line.rstrip()
    print '''
    Hieronder zie je het wat de code is met with en as open je het bestand en with closed het bestand automatisch:
    with open(bestand) as f:
        for line in f:
            print '    ' + line.rstrip()
    '''
    print_keywords()
    start()

def elif_statement():
    os.system('clear')
    num = int(raw_input("Kies een nummer:"))
    if (num < 5):
        print "Het gekozen getal %d is kleiner dan 5." % num
    elif (num == 5):
        print "Het gekozen getal %d is gelijk aan 5." % num
    else:
        print "Het gekozen getal %d is groter dan 5." % num
    raw_input("Druk op Enter> ")
    print '''
        if (num < 5):
            print "Het gekozen getal %d is kleiner dan 5." % num
        elif (num == 5):
            print "Het gekozen getal %d is gelijk aan 5." % num
        else:
            print "Het gekozen getal %d is groter dan 5." % num
        '''
    raw_input("Druk op Enter> ")
    print_keywords()
    start()

def global_statement():
    os.system('clear')
    def global_functie():
        global x # nu defineer je met global in deze functie dat de variable ook buiten de functie gebruikt kan worden.
        x = 155
        print x
    global_functie()
    print x # dit is de x variabele van in de functie
    print '''Je kunt een variable in een functie laten gelden voor de gehele uitvoering, dus buiten de functie met global
           ie: def global_functie():
                   global x
                   x = 155
                   print x
                   global_functie()
               print x'''
    print_keywords()
    start()

def or_statement():
    os.system('clear')
    num = int(raw_input("Kies nummer 5 of 9: "))
    if (num == 5 or num == 9):
        print "Gelukkig je kan de nummers 5 en 9 vinden op je toestenbord"
        print " if (num == 5 or num == 9):"
        print ""
        print "Dit was een voorbeeld van het OR statement"
        raw_input("Enteren>>>>")
        os.system('clear')
        print_keywords()
        start()
    else:
        print "Fout! kun je de nummers 5 of 9 echt niet vinden"
        raw_input("Enter drukken> ")
        or_statement()
       
def assert_statement():
    os.system('clear')
    num = int(raw_input("Om een error te krijgen, kies een nummer groter dan 5: "))
    assert num < 5, "Error,  nummer moet kleiner zijn dan 5!!"
    raw_input("Druk op enter: ")
    print_keywords()
    start()

def pass_keyword():  
    os.system('clear') # clear screen met de import os module 
    pass # negeer deze functie, code hem later. Als je deze functie in een class stopt krijg je geen error met pass.
    print_keywords()
    start()

def yield_keyword():
    pass
    #def simple_generator():
   #     os.system('clear')
    #    yield 1
    #    yield 2
    #    yield 3
       # for value in simple_generator():
        #    print(value)
       # our_generator = simple_generator
       # next(our_generator)
       # next(our_generator)
       # next(our_generator)
       # print_keywords()
       # start()
    #yield_keyword()

def break_statement():
    for letter in "Dit is een string":
        if letter == 'e':
            break
        print "Current letter:", letter
    print "Current letter stop bij:", letter
    print '''for letter in "Dit is een string":
    275         if letter == 'e':
    276             break
    277         print "Current letter:", letter
    278     print "Current letter stop bij:", letter'''

def except_statement():
    try:
        x = int(raw_input("Kies een nummer: (kies een letter voor de except error) "))
        print "Goedzo!"
        print_keywords()
        start()
    except ValueError:
        print "Oops dat was een letter en geen nummer!!"
        except_statement()

class class_statement:
    pass
#    var_text =  "Dit is een Python voorbeeld"
#    var_moeilijk = "makkelijk"
    
#    def functie_roepen(self, yname):
#        object1.yname = yname

# object1 = class_statement()
# object1.functie_roepen("Dave")
# object1.var_text

# print class_statement.var_text 
# print class_statement.var_moeilijk

def exec_statement():
    os.system('clear')
    print "Het exec statement is er om python code uit te voeren in een string."
    print "ie:"
    print ""
    een_variable = 'print "Dit is een python statement in een string"'
    exec een_variable
    print ""
    print ""
    print ""
    print '''Dit is de code:
    een_variable = 'print "Dit is een python statement in een string"'
    exec een_variable'''
    print ""
    print ""
    print ""
    raw_input("Druk op enter om door te gaan...")
    print_keywords()
    start()

def diff_between_for_while():
    os.system('clear')
    print '''Yes, there is a huge difference between while and for.
    The for statement iterates through a collection or iterable object or generator function.
    The while statement simply loops until a condition is False.
    It isn't preference. It's a question of what your data structures are.
    Often, we represent the values we want to process as a range (an actual list), or xrange (which generates the values). This gives us a data structure tailor-made for the for statement.
    Generally, however, we have a ready-made collection: a set, tuple, list, map or even a string is already an iterable collection, so we simply use a for loop.
    In a few cases, we might want some functional-programming processing done for us, in which case we can apply that transformation as part of iteration. The sorted and enumerate functions apply a transformation on an iterable that fits naturally with the for statement.
    If you don't have a tidy data structure to iterate through, or you don't have a generator function that drives your processing, you must use while.
'''
    print ""
    print ""
    print ""
    raw_input("Druk op Enter")
    os.system('clear')
    print_keywords()
    start()

def raise_statement():
    level = int(raw_input("Geef een nummer kleiner dan 1 voor foutmelding: "))
    if level < 1:
        raise Exception("Verkeerd nummer, voer opnieuw in", level)
    else:
        print "Goed nummer", level
        raw_input("Druk op Enter> ")
        print_keywords()
        start()

def continue_statement():
    while True:
        s = raw_input("Schrijf iets (langer dan 5 tekens, continue) of type quit (break uit de loop): ")
        if s == 'quit':
            break
        if len(s) < 5:
            continue
        print "We hebben een woord groter dan 5 tekens en continue."
        print_keywords()
        start()

def finally_statement():
    try:
        x = int(raw_input("Kies een nummer: (kies een letter voor de except error) "))
        print "Goedzo!"
    except Exception:
        print "Oops dat was een letter en geen nummer!!"
        finally_statement()
    else:
        os.system('clear')
        print "else statement wordt uitgevoerd"
        print ""
        print ""
        print ""
        print ""
        raw_input("Druk op de enterknop...")
    finally:
        os.system('clear')
        print "Deze code na finally wordt ALTIJD uitgevoerd."
        print ""
        print "als je een except clause gebruikt en je wilt finally uitvoeren, altijd else gebruiken"
        print ""
        raw_input("Druk op de enterknop...")
        print_keywords()
        start()

def is_statement():
    os.system('clear')
    print "Het 'is' statement is precies gelijk aan == ."
    print ""
    print ""
    print ""
    raw_input("Druk op enter de knop.")
    print_keywords()
    start()

def return_statement():
    def add(nummer1, nummer2):
        print "Optellen %d + %d" % (nummer1, nummer2)
        return nummer1 + nummer2
    opgeteld = add(5, 60)
    print opgeteld
    raw_input("Enteren")
    os.system('clear')
    print_keywords()
    start()

def lambda_function():
    func = lambda x : x * 3 # volgens mij wordt hier een variable omgezet naar functie.
    print func(3)
    print "Dit is lambda"

def datatypes_func():
    os.system('clear')
    print "1 + 1 == 2"
    print 1 + 1 == 2
    print ""
    print "1 + 1 == 3"
    print 1 + 1 == 3
    print ""
    print None
    print "None is een datatype wat eigenlijk niks betekent"
    print ""
    print ""
    print "Print some strings:"
    print "Dit is een string."
    print "Een string is een letter of combinatie letter/woorden of zinnen."
    print "Het tegengestelde van een string is een int ofwel een cijfer."
    print ""
    print ""
    print "Print some numbers:"
    print "Dit is een nummer ", 3
    print 3 + 3
    print 4 * 5
    print "Met nummer ofwel int kun je rekenenen."
    print ""
    print ""
    print "Print some floats:"
    print "Floats zijn nummers met decimale.n"
    print "2.4 + 3.6"
    print 2.4 + 3.6
    print ""
    print ""
    print "Print some lists"
    print "nummer_list = [1, 2, 3, 4, 5]"
    nummer_list = [1, 2, 3, 4, 5]
    print nummer_list
    print "string_list = [koe, ezel, hond, kat, varken]"
    string_list = ['koe', 'ezel', 'hond', 'kat', 'varken']
    print string_list

def string_esc_func():
    os.system('clear')
    print "Hieronder worden escape sequences uitgeschreven:"
    print ""
    print "Om een backslash in een string te krijgen: \\ dus \\\\ en bij die 2 weergegeven staan er in werkelijkheid 4 backslashes"
    print ""
    print "Wat doet \'. die quote wordt dus weergegven met een backslash ervoor ie: \\\'"
    print ""
    print "De backslash escaped ook een \". ie: \\\"."
    print ""
    print "print \a."
    

print_keywords()
start()
