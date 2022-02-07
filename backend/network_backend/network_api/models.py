from django.db import models

# Create your models here.

INITIAL_RELATION_NAME = 'attend\n'
INITIAL_NETWORK_ID = 'UP000315683'

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
        return str(self.network_id)

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
    i = 0
    for verb in verbs:
        relation = Relation(id = relations[i], name = verb)
        relation.save()
        i += 1

def init_data():
    RELATION_DATA_EXIST = Relation.objects.filter(name = INITIAL_RELATION_NAME).exists()
    if not RELATION_DATA_EXIST:
        init_relations_data()

try:
    init_data()
except:
    print('init database...')
