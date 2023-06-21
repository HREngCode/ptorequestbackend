from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import PtoRequest
from .serializers import PtoRequestSerializer


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_pto_requests(request):
        ptorequests = PtoRequest.objects.all()
        serializer = PtoRequestSerializer(ptorequests, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_request_by_supervisor(request):
    supervisor_param = request.query_params.get('supervisor')
    sort_param = request.query_params.get('sort')
    pto_requests = PtoRequest.objects.all()
    if supervisor_param:
        pto_requests = pto_requests.filter(employee__supervisor_number=supervisor_param)
    if sort_param:
        pto_requests = pto_requests.order_by(sort_param)
    serializer = PtoRequestSerializer(pto_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_request_by_employee_number(request):
    employee_param = request.query_params.get('employee')
    sort_param = request.query_params.get('sort')
    pto_requests = PtoRequest.objects.all()
    if employee_param:
        pto_requests = pto_requests.filter(employee__employee_number=employee_param)
    if sort_param:
        pto_requests = pto_requests.order_by(sort_param)
    serializer = PtoRequestSerializer(pto_requests, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def pto_request_create(request):
    serializer = PtoRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) 
def pto_request_detail(request, pk):
    pto_request = PtoRequest.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            serializer = PtoRequestSerializer(pto_request)
            return Response(serializer.data)
        except PtoRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = PtoRequestSerializer(pto_request, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        pto_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_request_by_employee_id(request):
#     employee_param = request.query_params.get('employee')
#     sort_param = request.query_params.get('sort')
#     pto_requests = PtoRequest.objects.all()
#     if employee_param:
#         pto_requests = pto_requests.filter(employee__id=employee_param)
#     if sort_param:
#         pto_requests = pto_requests.order_by(sort_param)
#     serializer = PtoRequestSerializer(pto_requests, many=True)
#     return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([AllowAny])
def pto_request_approve(request, pk):
    if request.method == 'PATCH':
        pto_request = PtoRequest.objects.get(pk=pk)
        serializer = PtoRequestSerializer(pto_request, data=request.data, partial=True)
        if serializer.is_valid():
            pto_request = serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_request_by_employee_id(request, id):
    pto_requests = request.query_params.get(id)
    pto_requests = PtoRequest.objects.all()
    pto_requests = pto_requests.filter(employee__id=id)
    serializer = PtoRequestSerializer(pto_requests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_request_by_id(request, id):
    pto_requests = request.query_params.get(id)
    pto_requests = PtoRequest.objects.all()
    pto_requests = pto_requests.get(id=id)
    serializer = PtoRequestSerializer(pto_requests)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_request_by_employee_number(request, id):
    pto_requests = request.query_params.get(id)
    pto_requests = PtoRequest.objects.all()
    pto_requests = pto_requests.filter(employee__employee_number=id)
    serializer = PtoRequestSerializer(pto_requests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_request_by_supervisor_number(request, id):
    pto_requests = PtoRequest.objects.all()
    pto_requests = pto_requests.filter(employee__supervisor_number=id)
    serializer = PtoRequestSerializer(pto_requests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



