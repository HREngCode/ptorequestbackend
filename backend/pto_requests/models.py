from django.db import models
from employees.models import Employee


# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class PtoRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_requested = models.DateField()
    hours_requested = models.DecimalField(max_digits=7, decimal_places=4)
    approved = models.BooleanField(default=False)