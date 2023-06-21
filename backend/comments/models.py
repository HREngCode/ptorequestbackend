from django.db import models
from pto_requests.models import PtoRequest
from employees.models import Employee

# Create your models here.


class Comment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pto_request = models.ForeignKey(PtoRequest, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)