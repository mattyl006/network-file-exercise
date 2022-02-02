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
