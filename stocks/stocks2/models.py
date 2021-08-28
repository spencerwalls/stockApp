from django.db import models

# These classes represent their respective models in the database

class Credential(models.Model):
    email = models.CharField(max_length=36)
    password = models.CharField(max_length=36)

    def __call__(self):
        return self

class Stock(models.Model):
    ticker = models.CharField(max_length=12)

    def __str__(self):
        return self.ticker 

class Wallet(models.Model):
    balance = models.CharField(max_length=36)

    def __str__(self):
        return self.balance