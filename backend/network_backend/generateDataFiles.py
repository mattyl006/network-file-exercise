#!/usr/bin/python3

import re

with open('network_file_no1.net', 'r') as file:
        DATA = file.read().replace('\n', ' | ')

def getRelations():
    allRelations = re.findall(r'[0-9]+ \|', DATA)
    relations = set()
    for relation in allRelations:
        relations.add(int(relation[0:-2]))
    return relations

def getNetworkIds():
    allNetworkIds = re.findall(r'UP[0-9]*[0-9]\t', DATA)
    networkIds = set()
    for id in allNetworkIds:
        networkIds.add(id[0:-1])
    return networkIds

def generateRelations():
    relations = getRelations()
    relationsFile = open("relations.txt", "x")
    for r in relations:
        relationsFile.write(str(r) + '\n')
    print('\n relations file generated!')

def generateNetworkIds():
    networkIds = getNetworkIds()
    networkIdsFile = open("networkIds.txt", "x")
    for n in networkIds:
        networkIdsFile.write(str(n) + '\n')
    print('\n network ids file generated!')

generateRelations()
generateNetworkIds()
