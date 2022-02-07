#!/usr/bin/python3

import re

with open('network_file_no1.net', 'r') as file:
    data = file.read().replace('\n', ' | ')

allRelations = re.findall(r'[0-9]+ \|', data)

relations = set()

for relation in allRelations:
    relations.add(int(relation[0:-2]))

print('\nRelations: ' + str(relations))
print('\nCount of relations: ' + str(len(relations)) + '\n')

print(data[0:1000])

allElements = re.findall(r'UP[0-9]*[0-9]\t', data)

elements = set()

for element in allElements:
    elements.add(element[0:-1])

print('\nExample elements: ' + str(elements)[0:1005])
print('\nCount of elements: ' + str(len(elements)) + '\n')

elementsAndHisRelations = []
i = 0
for element in elements:
    elementsAndHisRelations.append(set(re.findall(r'' + str(element) + r'\t[0-9]', data)))
    i += 1
    print(i)
    if i == 4:
        break

print(elementsAndHisRelations)
