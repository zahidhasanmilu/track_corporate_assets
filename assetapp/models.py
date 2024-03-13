from django.utils import timezone
from django.db import models

# Create your models here.


# The `Company` class in Python defines a model with fields for name, creation timestamp, and last
# update timestamp.
class Company(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# This Python class defines an Employee model with fields for company, name, and department.
class Employee(models.Model):
    company = models.ForeignKey(
        Company, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    

# The class `Assets` defines a model with fields for asset name, brand, company, condition,
# manufacturer, serial number, issued status, and purchase date.
class Assets(models.Model):
    CONDITION_CHOICE = (('Excellent', 'Excellent'),
                        ('Fair', 'Fair'), ('Damaged', 'Damaged'))

    name = models.CharField(max_length=100)

    brand = models.CharField(max_length=50, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    current_condition = models.CharField(
        max_length=50, choices=CONDITION_CHOICE, default='Fair')
    manufacturer = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=255, unique=True)
    issued = models.BooleanField(default=False)
    purchased_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['purchased_date']

    def __str__(self):
        return self.name + " " + self.manufacturer


# The `AssetsLog` class defines a model with fields for tracking asset checkout and return information
# for employees.
class AssetLog(models.Model):
   asset = models.ForeignKey(Assets, related_name= 'asset', on_delete=models.CASCADE, null=True, blank=True)
   employee = models.ForeignKey(Employee, related_name= 'employee', on_delete=models.CASCADE, null=True, blank=True)
   checkout_date = models.DateTimeField()
   return_date = models.DateTimeField(null=True, blank=True)
   checkout_condition = models.TextField()
   return_condition = models.TextField(null=True, blank=True)