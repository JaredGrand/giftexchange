"""This program is designed to take a list of names and randomize who gives presents to who in a gift exchange"""

import random

def people_list():
    str1 = "Please list the names of the participants separated by commas: "
    return input(str1)

def format_list(somelist):
    somelist = somelist.split(',')
    newlist = []
    for name in somelist:
        name = name.strip()
        newlist.append(name)
    return newlist

def draw_names(names):
    names = format_list(names)
    exchange = {}
    taken = []
    for name in names:
        recipient = random.choice(names)
        while recipient == name or recipient in taken:
            if (len(names) - len(taken)) == 1:
                print("One person was left to draw and only their name was left! Please try again.")
                break
            else:
                recipient = random.choice(names)
        exchange[name] = recipient
        taken.append(recipient)
    return exchange

def results(drawing):
    for key in drawing:
        print(f"{key} has {drawing[key]}.")

def final():
    names = people_list()
    exchange = draw_names(names)
    results(exchange)

if __name__ == '__main__':
    final()
