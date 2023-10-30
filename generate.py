import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudDemo.settings') #give project name
# set DJANGO_SETTINGS_MODULE=crudDemo.settings <<<<<add this line into the command line
import django
django.setup()

from crudApp.models import *  # give proper appname 
from faker import Faker
from random import *
faker=Faker()
def generate(n):
    for i in range(n):
        fsno=randint(100,999)   #give the datas you defined in models.py
        fsname=faker.name()
        fsage=randint(18,22)
        fssec=faker.city()
        stud_record=Student.objects.get_or_create(Sno=fsno,Sname=fsname,Sage=fsage,Sadrs=fssec)
        print(f"list of details created for {n} students")
generate(25)
