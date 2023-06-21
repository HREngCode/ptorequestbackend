from rest_framework import status
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Employee
from .serializers import EmployeeSerializer


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


# Get all employees
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_list(request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


# Get name by user id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_name_by_user_id(request, user):
    employees = request.query_params.get(user)
    employees = Employee.objects.all()
    employees = employees.get(user_id=user)
    serializer = EmployeeSerializer(employees)
    print(employees)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Get name by employee number
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_name_by_employee_number(request, user):
    employees = request.query_params.get(user)
    employees = Employee.objects.all()
    employees = employees.get(employee_number=user)
    serializer = EmployeeSerializer(employees)
    print(employees)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Get by supervisor number
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_name_by_supervisor_number(request, id):
    employees = request.query_params.get(id)
    employees = Employee.objects.all()
    employees = employees.filter(supervisor_number=id)
    serializer = EmployeeSerializer(employees, many=True)
    print(employees)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Get employee by parameters
@api_view(['GET'])
@permission_classes([AllowAny])
def get_by_employee_param(request):
    employee_param = request.query_params.get('employee_number')
    sort_param = request.query_params.get('sort')
    employees = Employee.objects.all()
    if employee_param:
        employees = employees.filter(employee_number=employee_param)
    if sort_param:
        employees = employees.order_by(sort_param)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


# Create new Employee
@api_view(['POST'])
@permission_classes([AllowAny]) 
def employee_create(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get, Update, or Delete Employee Detail
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny]) 
def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PATCH'])
@permission_classes([AllowAny])
def employee_update_pto_balance(request, pk):
    if request.method == 'PATCH':
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            employee = serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    