"""This program is designed to take a list of names and randomize who gives presents to who in a gift exchange"""

import random

def people_list():
    str1 = "Please list the names of the participants separated by commas: "
    return input(str1)

list1 = people_list()
list1 = list1.split(',')

exchange = {}
taken = []
for name in list1:
    print(f"Name: {name}")
    print(f"List1: {list1}")
    recipient = random.choice(list1)
    if (recipient == name) or (recipient in taken):
        recipient = random.choice(list1)
    print(f"Recipient: {recipient}")
    exchange[name] = recipient
    print(f"Exchange: {exchange}")
    taken.append(recipient)
    print(f"Taken: {taken}")
