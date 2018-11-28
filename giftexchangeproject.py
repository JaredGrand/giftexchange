"""This program is designed to take a list of names and randomize who gives presents to who in a gift exchange"""

import random

def people_list():
    str1 = "Please list the names of the participants separated by commas: "
    return input(str1)

list1 = people_list()
list1 = list1.split(',')

exchange = {}
for name in list1:
    exchange[name] = random.choice(list1)
