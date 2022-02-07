from django.db import models

# Create your models here.

INITIAL_RELATION_NAME = 'attend\n'
INITIAL_NETWORK_ID = 'UP000262375\n'

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
    surname = models.CharField(max_length=100)
    friends = models.ManyToManyField(Friend)
    relations = models.ManyToManyField(Relation)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' (' + str(self.network_id) + ')'

def init_relations_data():
    print('init relations data...')
    with open('verbs.txt', 'r') as file:
        verbs = file.readlines()
    with open('relations.txt', 'r') as file:
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
    with open('networkIds.txt', 'r') as file:
        networkIds = file.readlines()
    Friend.objects.bulk_create([Friend(
        **{'id' : int('98' + networkId[2:]), 'network_id' : networkId})
        for networkId in networkIds
    ])

    # friends_relations = [(), (), ...]

    # Friend.relations.through.objects.bulk_create([
    #     Friend.relations.through(friend_id = f_id, relation_id = r_id)
    #     for (f_id, r_id) in friends_relations
    # ])

def init_data():
    RELATION_DATA_EXIST = Relation.objects.filter(name = INITIAL_RELATION_NAME).exists()
    FRIENDS_DATA_EXIST = Friend.objects.filter(network_id = INITIAL_NETWORK_ID).exists()
    if not RELATION_DATA_EXIST:
        init_relations_data()
    if not FRIENDS_DATA_EXIST:
        init_friends_data()
try:
    init_data()
except:
    print('init database...')
