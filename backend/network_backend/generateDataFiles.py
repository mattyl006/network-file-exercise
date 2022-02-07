#!/usr/bin/python3

import re

def getRelations():
    with open('network_file_no1.net', 'r') as file:
        data = file.read().replace('\n', ' | ')
        allRelations = re.findall(r'[0-9]+ \|', data)
        relations = set()
        for relation in allRelations:
            relations.add(int(relation[0:-2]))
        return relations

relations = getRelations()

relationsFile = open("relations.txt", "x")

for r in relations:
    relationsFile.write(str(r) + '\n')

print('\n relations file generated!')
