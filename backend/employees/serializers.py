from rest_framework import serializers
from .models import Employee

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class EmployeeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Employee
        fields = ['id', 'employee_number', 'employee_first_name', 'employee_last_name', 'department', 'supervisor_number', 'hire_date', 'pto_balance', 
        'user', 'user_id', 'active', 'isSupervisor', 'isAdmin']
        depth = 1

    user_id = serializers.IntegerField(write_only=True)