from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Lists


#Class
#Small class
class Allergy(models.Model):
    allergy = models.CharField(max_length = 200)

    def __str__(self):
        return self.allergy
    
class Parking(models.Model):
    parking = models.CharField(max_length = 200)

    def __str__(self):
        return self.parking
    
#Priority Class
    
class TresoreryCompta(models.Model):
    moneyFlowName = models.CharField(max_length = 200)
    models.CharField(max_length = 100, blank = True, null = True)
    amount = models.FloatField()
    currency = models.CharField(max_length = 10, blank = True, null = True)
    category = models.CharField(max_length = 100, blank = True, null = True)
    subCategory = models.CharField(max_length = 100, blank = True, null = True)
    pole = models.CharField(max_length = 100, blank = True, null = True)
    comment = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return self.moneyFlowName

#Master class

class AnimationContact(models.Model):
    userInCharge = models.ManyToManyField(User, blank = True)
    status = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    note = models.TextField(blank = True, null = True)
    stand = models.BooleanField(blank = True, null = True)
    activity = models.BooleanField(blank = True, null = True)
    prestation = models.BooleanField(blank = True, null = True)
    firstname = models.CharField(max_length = 100, blank = True, null = True)
    surname = models.CharField(max_length = 100, blank = True, null = True)
    namEntity = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200, blank = True, null = True)
    phone = models.CharField(max_length = 100, blank = True, null = True)
    addressRoad = models.CharField(max_length = 100, blank = True, null = True)
    addressNumber = models.CharField(max_length = 10, blank = True, null = True)
    addressCity = models.CharField(max_length = 100, blank = True, null = True)
    addressCountry = models.CharField(max_length = 50, blank = True, null = True)
    allergy = models.ManyToManyField(Allergy, blank = True)
    parking = models.ManyToManyField(Parking, blank = True)
    transportComment = models.TextField(blank = True, null = True)
    transportStatus = models.CharField(max_length = 100, blank = True, null = True)
    hotelComment = models.TextField(blank = True, null = True)
    hotelStatus = models.CharField(max_length = 100, blank = True, null = True)
    expense = models.ManyToManyField(TresoreryCompta, blank = True) 

    def __str__(self):
        return self.namEntity



