from django.db import models
from authentication.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_number = models.IntegerField(  )
    employee_first_name = models.CharField(max_length=30)
    employee_last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    supervisor_number = models.IntegerField( )
    hire_date = models.DateField(null=True)
    pto_balance = models.DecimalField(max_digits=7, decimal_places=4)
    active = models.BooleanField( )
    isSupervisor = models.BooleanField( )
    isAdmin = models.BooleanField( )

