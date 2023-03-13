from django.db import models

# Create your models here.

class Cars(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"Car is {self.brand} {self.year}"

class Repair(models.Model):
    repair_description = models.CharField(max_length = 100)
    repaired_date = models.DateField()
    cars = models.ManyToManyField(Cars)
    def __str__(self):
        return f"Car {self.cars} repair description: {self.repair_description} on {self.repaired_date}"