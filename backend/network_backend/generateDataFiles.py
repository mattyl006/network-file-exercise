#!/usr/bin/python3

import re2 as re
import names

with open('data_files/network_file_no1.net', 'r') as file:
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

def generateRelations(relations):
    relationsFile = open("data_files/relations.txt", "x")
    for r in relations:
        relationsFile.write(str(r) + '\n')
    print('\n relations file generated!')

def generateNetworkIds(networkIds):
    networkIdsFile = open("data_files/networkIds.txt", "x")
    for n in networkIds:
        networkIdsFile.write(str(n) + '\n')
    print('\n network ids file generated!')

def generateNames(networkIds):
    namesOfElements = set()
    while len(namesOfElements) != len(networkIds):
        namesOfElements.add(names.get_first_name() + ' ' + names.get_last_name())
    personsFile = open("data_files/persons.txt", "x")
    for n in namesOfElements:
        personsFile.write(str(n) + '\n')
    print('\n persons names generated!')

relations = getRelations()
networkIds = getNetworkIds()
generateRelations(relations)
generateNetworkIds(networkIds)
generateNames(networkIds)
