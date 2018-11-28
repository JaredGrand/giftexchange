"""This program is designed to take a list of names and randomize who gives presents to who in a gift exchange"""

import random

def people_list():
    """Asks for all participants in the gift exchange"""
    str1 = "Please list the names of the participants separated by commas: "
    return input(str1)

def format_list(somelist):
    """Formats a string into a clean list"""
    somelist = somelist.split(',')
    newlist = []
    for name in somelist:
        name = name.strip()
        newlist.append(name)
    return newlist

def draw_names(names):
    """Cycles through the list of names and draws someone"""
    names = format_list(names)
    exchange = {}
    taken = []
    for name in names:
        recipient = random.choice(names)
        while recipient == name or recipient in taken:
            """If someone draws their own name. Also avoids someone being drawn twice"""
            if (len(names) - len(taken)) == 1:
                """Scenario in which 1 person is left but their name is the only one left undrawn"""
                return "bang"
            else:
                recipient = random.choice(names)
        exchange[name] = recipient
        taken.append(recipient)
    return exchange

def results(drawing):
    """Prints the results of the drawing"""
    for key in drawing:
        print(f"\n{key} has {drawing[key]}.")

def final():
    """Incorporates all the above functions"""
    names = people_list()
    exchange = draw_names(names)
    while exchange == "bang":
        """Cycles through until there is a 'good' draw. No one is left w/o a name"""
        exchange = draw_names(names)
    results(exchange)

if __name__ == '__main__':
    final()
