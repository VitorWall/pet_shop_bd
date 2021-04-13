from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=70)
    specie = models.CharField(max_length=70)
    race = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Client(models.Model):
    CPF = models.IntegerField(11, primary_key=True)
    name = models.CharField(max_length=70)
    phone = models.IntegerField(11)
    vip_or_not = models.BooleanField()

    def __str__(self):
        return self.name

class Worker(models.Model):
    CPF = models.IntegerField(11, primary_key=True)
    name = models.CharField(max_length=70)
    job = models.CharField(max_length=70)
    salary = models.DecimalField(decimal_places=2)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    service_type = models.CharField(max_length=70)
    description = models.CharField(max_length=400)
    medium_duration = models.DurationField()
    def __str__(self):
        return self.service_type

class Unit:
    cep = models.IntegerField(8, primary_key=True)
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Stock:
    aplication = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    quantity = models.IntegerField(1)

    def __str__(self):
        return self.name

class Accommodation:
    number = models.IntegerField(1, primary_key=True)
    size = models.IntegerField(3)

    def __str__(self):
        return str(self.number)

class Room:
    number = models.IntegerField(1, primary_key=True)
    equipments = models.CharField(max_length=100)

    def __str__(self):
        return str(self.number)
    
