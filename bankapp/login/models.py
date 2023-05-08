from django.db import models
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from string import punctuation
from django.utils import timezone

# Create your models here.
class account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    holdername = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    dob = models.DateTimeField()
    credential = models.CharField(max_length=80)
    balance = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.holdername

class transaction(models.Model):
    id = models.AutoField(primary_key=True)
    acctId_from = models.IntegerField()
    acctId_to = models.IntegerField()
    ammount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"Transaction: {self.ammount}"