"""This program is designed to take a list of names and randomize who gives presents to who in a gift exchange"""

import random

def people_list():
    str1 = "Please list the names of the participants separated by commas: "
    return input(str1)

list1 = people_list()

def format_list(somelist):
    somelist = somelist.split(',')
    newlist = []
    for name in somelist:
        name = name.strip()
        newlist.append(name)
    return newlist

def draw_names(names):
    exchange = {}
    taken = []
    for name in names:
        recipient = random.choice(names)
        while recipient == name or recipient in taken:
            recipient = random.choice(names)
        exchange[name] = recipient
        taken.append(recipient)
    return exchange
