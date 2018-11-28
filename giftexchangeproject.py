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

def draw_names(newlist):
    exchange = {}
    taken = []
    for name in newlist:
        # print(f"Name: {name}")
        # print(f"List1: {list1}")
        recipient = random.choice(newlist)
        while recipient == name or recipient in taken:
            recipient = random.choice(newlist)
        # print(f"Recipient: {recipient}")
        exchange[name] = recipient
        # print(f"Exchange: {exchange}")
        taken.append(recipient)
        # print(f"Taken: {taken}")
    return exchange
