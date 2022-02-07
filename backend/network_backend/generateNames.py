#!/usr/bin/python3

import names

namesOfElements = set()

while len(namesOfElements) < 8500:
    namesOfElements.add(names.get_first_name() + ' ' + names.get_last_name())

print('\nNames of elements: ' + str(namesOfElements) + '\n')

print('\nCount of names: ' + str(len(namesOfElements)))
