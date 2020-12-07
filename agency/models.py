from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.manufacturer + ' ' + self.name
