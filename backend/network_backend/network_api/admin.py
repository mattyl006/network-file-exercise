from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Relation)
admin.site.register(Friend)
admin.site.register(Person)
