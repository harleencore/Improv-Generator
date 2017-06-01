import random
prompt = ""

def proceed():
    enter = raw_input(prompt)
    if enter == "X":
        exit()

def generate_opening_line():
    print(random.choice(list(open('opening_lines.txt'))))
    generator_generator()

def generate_hat_scene():
    print(random.choice(list(open('scenes_from_a_hat.txt'))))
    generator_generator()

def generator_generator():
    print "Type 1 for 'opening lines', and 2 for 'Scenes from a hat'"
    gen = raw_input("> ")
    if gen == "1":
        print "YEAH"
        generate_opening_line()
    elif gen == "2":
        generate_hat_scene()
    else:
        exit()

print "Hullo! I'm the improv script."
proceed()
print "We're going to play a game."
proceed()
print "The rules are simple. Pair up, pick a category and HAVE FUN!"
proceed()
print "There are two categories."
proceed()
print "The first is called 'Opening Lines'"
proceed()
print "The second is called 'Scenes from a hat'"
proceed()
print "'Opening lines' is self explanatory;"
print "We give you a line that you must begin the scene with"
proceed()
print "'Scenes from a hat' are quick fire scenes \n involving one or two people, and a couple of lines at most."
proceed()
print "OK LETS GO!"
proceed()

generator_generator()
