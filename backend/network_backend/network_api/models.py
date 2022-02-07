from django.db import models

# Create your models here.

class Friend(models.Model):
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return str(self.id)

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    network_id = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    friends = models.ManyToManyField(Friend)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)

INITIAL_NETWORK_ID = 'UP000315683'

def init_person_data():
    f = Friend(id = 98000263435)
    f.save()

    p = Person(id = 98000315683, network_id = INITIAL_NETWORK_ID, 
    name = 'Jan', surname = 'Kowalski')
    p2 = Person(id = 98000263435, network_id = 'UP000263435', name = 'Ania', surname = 'Kowalska')

    p.save()
    p2.save()

    p.friends.add(f)

    p.save()

try:
    DATA_EXIST = Person.objects.filter(network_id = INITIAL_NETWORK_ID).exists()
    if not DATA_EXIST:
        print('init persons data')
        init_person_data()
except:
    print('init database')
