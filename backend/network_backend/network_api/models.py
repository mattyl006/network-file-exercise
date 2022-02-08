from django.db import models
import re2 as re

# Create your models here.

INITIAL_RELATION_NAME = 'attend\n'
INITIAL_NETWORK_ID = 'UP000262375'

class Relation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name) + ' (' + str(self.id) + ')'

class Friend(models.Model):
    id = models.BigAutoField(primary_key=True)
    network_id = models.CharField(max_length=11, unique=True)
    relations = models.ManyToManyField(Relation)
    def __str__(self):
        return str(self.id) + ' (' + str(self.network_id)[:-1] + ')'

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    network_id = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField(Friend)
    relations = models.ManyToManyField(Relation)

    def __str__(self):
        return str(self.name) + ' (' + str(self.network_id) + ')'

def init_relations_data():
    print('init relations data...')
    with open('data_files/verbs.txt', 'r') as file:
        verbs = file.readlines()
    with open('data_files/relations.txt', 'r') as file:
        relations = file.readlines()
    if len(verbs) == len(relations):
        Relation.objects.bulk_create([Relation(
            **{'id' : relations[i], 'name' : verbs[i]})
            for i in range(len(relations))
        ])
    else:
        print('ERROR: verbs.txt has not the same count of elements like relations.txt')

def init_friends_data():
    print('init friends data...')
    with open('data_files/networkIds.txt', 'r') as file:
        networkIds = file.readlines()
    Friend.objects.bulk_create([Friend(
        **{'id' : int('98' + networkId[2:]), 'network_id' : networkId[:-1]})
        for networkId in networkIds
    ])

def init_friends_relations_association():
    print('init friends <-> relations associations...')
    with open('data_files/network_file_no1.net', 'r') as file:
        data = file.read().replace('\n', ' | ')
    relations = set(re.findall(r'[0-9]+ \|', data))
    friends_relations = []
    i = 0
    for relation in relations:
        elementAndHisRelations = (set(re.findall(r'UP[0-9]*[0-9]\t' + relation[:-2], data)))
        for element in elementAndHisRelations:
            item = (int('98' + element[2:11]), int(element[12:]))
            friends_relations.append(item)
            i += 1
            if i == 70000:
                print("almost there...")
    Friend.relations.through.objects.bulk_create([
        Friend.relations.through(friend_id = f_id, relation_id = r_id)
        for (f_id, r_id) in friends_relations
    ])

def init_persons_data():
    print('init persons data...')
    with open('data_files/networkIds.txt', 'r') as file:
        networkIds = file.readlines()
    with open('data_files/persons.txt', 'r') as file:
        persons = file.readlines()
    if len(networkIds) == len(persons):
        Person.objects.bulk_create([Person(
            **{'id' : int('98' + networkIds[i][2:]), 
            'network_id' : networkIds[i][:-1], 'name' : persons[i][:-1]})
            for i in range(len(networkIds))
        ])
    else:
        print('ERROR: persons.txt has not the same count of elements like networkIds.txt')

def init_persons_relations_association():
    print('init persons <-> relations associations...')
    with open('data_files/network_file_no1.net', 'r') as file:
        data = file.read().replace('\n', ' | ')
    relations = set(re.findall(r'[0-9]+ \|', data))
    persons_relations = []
    i = 0
    for relation in relations:
        elementAndHisRelations = (set(re.findall(r'(UP[0-9]*[0-9]\t)(?:UP[0-9]*[0-9]\t)(' + relation[:-2] + ')', data)))
        for element in elementAndHisRelations:
            item = (int('98' + element[0][2:11]), int(element[1]))
            persons_relations.append(item)
            i += 1
            if i == 70000:
                print("almost there...")
    Person.relations.through.objects.bulk_create([
        Person.relations.through(person_id = p_id, relation_id = r_id)
        for (p_id, r_id) in persons_relations
    ])

    
def init_data():
    RELATION_DATA_EXIST = Relation.objects.filter(name = INITIAL_RELATION_NAME).exists()
    FRIENDS_DATA_EXIST = Friend.objects.filter(network_id = INITIAL_NETWORK_ID).exists()
    PERSONS_DATA_EXIST = Person.objects.filter(network_id = INITIAL_NETWORK_ID).exists()
    if not RELATION_DATA_EXIST:
        init_relations_data()
    if not FRIENDS_DATA_EXIST:
        init_friends_data()
        init_friends_relations_association()
    if not PERSONS_DATA_EXIST:
        init_persons_data()
        init_persons_relations_association()

try:
    init_data()
except:
    print('init database...')
