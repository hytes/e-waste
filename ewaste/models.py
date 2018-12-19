from django.db import models

class General(models.Model):
    location = models.CharField(max_length=250)
    joint = models.CharField(max_length=500)
    time = models.DateTimeField()
    
    def __str__(self):
        return self.location + '-' + self.joint

class Specific(models.Model):
    location = models.CharField(max_length=250)
    quantity = models.CharField(max_length=500)
    time = models.DateTimeField()

    def __str__(self):
        return self.location + '-' + self.quantity
