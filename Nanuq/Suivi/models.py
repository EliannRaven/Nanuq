from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.

#Lists

TRESORERY_STATUS = [
    ('BILL_TO_DO', 'Facture à faire'),
    ('WAITING', 'En attente de payement'),
    ('TO_PAY', 'A payer'),
    ('PAYED', 'Payé')
]

CURRENCY = [
    ('CHF', 'CHF'),
    ('EUR', 'EUR'),
    ('USD', 'USD'),
    ('JPY', 'JPY'),
]

PANEL_TYPE = [
    ('WOOD', 'Bois'),
    ('FELT', 'Feutre'),
    ('METAL', 'Métal'),
]

CONTACT_STATUS = [
    ('NOT_STARTED', 'Pas commencé'),
    ('WAITING_CONTACT', 'En attente du contact'),
    ('WAITING_COMMITTEE', 'En attente de nous'),
    ('FORM_SENT', 'Formulaire envoyé'),
    ('FORM_ANSWERED', 'Formulaire répondu'),
    ('CONTRACT_TO_SEND', 'Contrat à envoyer'),
    ('WAITING_CONTRACT', 'Contrat envoyé'),
    ('CONTRACT_SIGNED', 'Contrat signé'),
    ('CONTRACT_CANCELLED', 'Contrat annulé'),
    ('CANCELLED', 'Contact annulé'),
]

CONTACT_LOG_STATUS = [
    ('NOT_STARTED', 'Pas commencé'),
    ('WAITING_CONTACT', 'En attente du contact'),
    ('WAITING_COMMITTEE', 'En attente de nous'),
    ('OK', 'Affaire conclue'),
    ('CANCELLED', 'Annulé'),
]


#Class
#Small class
class Allergy(models.Model):
    allergy = models.CharField(max_length = 200)
    comment = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.allergy
    
class Parking(models.Model):
    parking = models.CharField(max_length = 200)
    comment = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.parking
    
#Priority Class
    
class TresoreryCompta(models.Model):
    moneyFlowName = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    amount = models.FloatField()
    currency = models.CharField(max_length = 10, choices = CURRENCY, default = 'CHF', blank = True, null = True)
    category = models.CharField(max_length = 100, blank = True, null = True) #LIST
    subCategory = models.CharField(max_length = 100, blank = True, null = True) #LIST
    pole = models.CharField(max_length = 100, blank = True, null = True) #LIST => Voir même carrément une class => A voir quand je ferai l'app user.
    status = models.CharField(max_length = 100, choices = TRESORERY_STATUS, blank = True, null = True)
    comment = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return self.moneyFlowName
    
class TresoreryBudget(models.Model):
    moneyLoad = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    amount = models.PositiveIntegerField(blank = True, null = True)
    spent = models.PositiveIntegerField(blank = True, null = True)
    currency = models.CharField(max_length = 10, choices = CURRENCY, default = 'CHF', blank = True, null = True)
    category = models.CharField(max_length = 100, blank = True, null = True) #LIST
    subCategory = models.CharField(max_length = 100, blank = True, null = True) #LIST
    pole = models.CharField(max_length = 100, blank = True, null = True) #LIST => Voir même carrément une class => A voir quand je ferai l'app user.
    comment = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return self.moneyLoad   

class Room(models.Model):
    location = models.CharField(max_length = 20)
    comment = models.TextField(blank = True, null = True)
    table = models.PositiveIntegerField(blank = True, null = True)
    chair = models.PositiveIntegerField(blank = True, null = True)
    panel = models.PositiveIntegerField(blank = True, null = True)
    panelType = models.CharField(max_length = 50, choices = PANEL_TYPE, blank = True, null = True)
    conformation = models.ImageField(upload_to='images/', blank = True, null = True)
    water = models.BooleanField(blank = True, null = True)
    elec = models.FloatField(default = 500)
    elecComment = models.TextField(blank = True, null = True)
    secuCheck = models.BooleanField(blank = True, null = True)

    def __str__(self):
        return self.location

class Planning(models.Model):
    location = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True, blank = True)
    #activity = models.ForeignKey(AnimationActivity, on_delete = models.SET_NULL, null = True, blank = True)
    comment = models.TextField(blank = True, null = True)
    day = models.DateField()
    start = models.DateTimeField()
    duration = models.PositiveIntegerField() #always in minutes
    end = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
    # Calculate end time based on start and duration
        if self.start and self.duration:
            self.end = self.start + timedelta(minutes=self.duration)

        # Call the original save method to save the instance
        super().save(*args, **kwargs)

    def __str__(self):
        return f"location: {self.location} - start: {self.start}"
    
class LogInventaire(models.Model):
    materialName = models.CharField(max_length = 200, blank = True, null = True)
    comment = models.TextField(blank = True, null = True)
    category = models.CharField(max_length = 100, blank = True, null = True) #LIST
    status = models.CharField(max_length = 100, blank = True, null = True) #LIST
    acquisitionWay = models.CharField(max_length = 100, blank = True, null = True) #LIST
    amount = models.PositiveIntegerField(blank = True, null = True)
    unit = models.CharField(max_length = 20, blank = True, null = True)
    storageLocation = models.CharField(max_length = 100, blank = True, null = True) #LIST
    #jiUsedFor = models.ForeignKey()
    elec = models.FloatField(default = 500)
    elecComment = models.TextField(blank = True, null = True) 

    def __str__(self):
        return self.materialName

#Master class

class AnimationContact(models.Model):
    userInCharge = models.ForeignKey(User, on_delete = models.SET_NULL, blank = True, null = True) #in List
    status = models.CharField(max_length = 100, choices = CONTACT_STATUS) #in List
    description = models.TextField(blank = True, null = True)
    note = models.TextField(blank = True, null = True)
    stand = models.BooleanField(blank = True, null = True) #in List
    activity = models.BooleanField(blank = True, null = True) #in List
    prestation = models.BooleanField(blank = True, null = True) #in List
    firstname = models.CharField(max_length = 100, blank = True, null = True)
    surname = models.CharField(max_length = 100, blank = True, null = True)
    namEntity = models.CharField(max_length = 100) #in List
    email = models.EmailField(max_length = 200, blank = True, null = True)
    phone = models.CharField(max_length = 100, blank = True, null = True)
    addressRoad = models.CharField(max_length = 100, blank = True, null = True)
    addressNumber = models.CharField(max_length = 10, blank = True, null = True)
    addressCity = models.CharField(max_length = 100, blank = True, null = True)
    addressCountry = models.CharField(max_length = 50, blank = True, null = True)
    allergy = models.ManyToManyField(Allergy, blank = True)
    parking = models.ManyToManyField(Parking, blank = True)
    transportComment = models.TextField(blank = True, null = True)
    transportStatus = models.CharField(max_length = 100, choices = CONTACT_LOG_STATUS, default = 'NOT_STARTED', blank = True, null = True)
    hotelComment = models.TextField(blank = True, null = True)
    hotelStatus = models.CharField(max_length = 100, choices = CONTACT_LOG_STATUS, default = 'NOT_STARTED', blank = True, null = True)
    expense = models.ManyToManyField(TresoreryCompta, blank = True) 

    def __str__(self):
        return self.namEntity

class AnimationStand(models.Model):
    contact = models.ForeignKey(AnimationContact, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    comment= models.TextField(blank = True, null = True)
    category = models.CharField(max_length = 100, blank = True, null = True) #LIST
    standMoney = models.ForeignKey(TresoreryCompta, on_delete = models.SET_NULL, null = True, blank = True)
    location = models.CharField(max_length = 20, blank = True, null = True)
    table = models.PositiveIntegerField(blank = True, null = True)
    chair = models.PositiveIntegerField(blank = True, null = True)
    panel = models.PositiveIntegerField(blank = True, null = True)
    panelType = models.CharField(max_length = 50, choices = PANEL_TYPE, blank = True, null = True)
    vaisselle = models.TextField(blank = True, null = True)
    water = models.BooleanField(blank = True, null = True)
    elec = models.FloatField(default = 500, blank = True, null = True)
    elecComment = models.TextField(blank = True, null = True)
    secuCheck = models.BooleanField(blank = True, null = True)
    deliveryTiming = models.DateTimeField(blank = True, null = True)  
    descriptionComm = models.TextField(blank = True, null = True)
    imageComm = models.ImageField(upload_to='images/', blank = True, null = True)

    def __str__(self):
        return self.name
    
class AnimationActivity(models.Model):
    contact = models.ForeignKey(AnimationContact, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    activityMoney = models.ForeignKey(TresoreryCompta, on_delete = models.SET_NULL, null = True, blank = True)
    comment= models.TextField(blank = True, null = True)
    category = models.CharField(max_length = 100, blank = True, null = True) #LIST
    descriptionComm = models.TextField(blank = True, null = True)
    imageComm = models.ImageField(upload_to='images/', blank = True, null = True)
    arrivalTiming = models.DateTimeField(blank = True, null = True)
    staffNeeded = models.PositiveIntegerField(blank = True, null = True)
    staffPreRequis = models.TextField(blank = True, null = True)
    staffActivityDescription = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

class AnimationPrestation(models.Model):
    contact = models.ForeignKey(AnimationContact, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    prestationMoney = models.ForeignKey(TresoreryCompta, on_delete = models.SET_NULL, null = True, blank = True)
    comment= models.TextField(blank = True, null = True)
    category = models.CharField(max_length = 100, blank = True, null = True) #LIST
    descriptionComm = models.TextField(blank = True, null = True)
    imageComm = models.ImageField(upload_to='images/', blank = True, null = True)
    staffNeeded = models.PositiveIntegerField(blank = True, null = True)
    staffPreRequis = models.TextField(blank = True, null = True)
    staffActivityDescription = models.TextField(blank = True, null = True)
    technicalSheet = models.TextField(blank = True, null = True)
    satCheck = models.BooleanField(blank = True, null = True)

    def __str__(self):
        return self.name