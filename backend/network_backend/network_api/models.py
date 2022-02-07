from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    network_id = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)

INITIAL_NETWORK_ID = 'UP000315683'

def init_person_data():
    p = Person(network_id = INITIAL_NETWORK_ID, name = 'Jan', surname = 'Kowalski')
    p.save()

try:
    DATA_EXIST = Person.objects.filter(network_id = INITIAL_NETWORK_ID).exists()
    if not DATA_EXIST:
        print('init persons data')
        init_person_data()
except:
    print('init database')
