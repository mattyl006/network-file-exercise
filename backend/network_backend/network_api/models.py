from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)

def init_person_data():
    p = Person(id = 98000315683, name = 'Jan', surname = 'Kowalski')
    p.save()

INITIAL_ID = 98000315683
DATA_EXIST = Person.objects.filter(id = INITIAL_ID).exists()

if not DATA_EXIST:
    print('init persons data')
    init_person_data()
