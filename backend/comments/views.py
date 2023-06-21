from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment
from .serializers import CommentSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

@api_view(['GET'])
@permission_classes([AllowAny])
def comments_list_by_employee(request, id):
        comments = request.query_params.get(id)
        queryset = Comment.objects.all()
        queryset = queryset.filter(employee_id=id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def comments_list_by_request(request, id):
        comments = request.query_params.get(id)
        queryset = Comment.objects.all()
        queryset = queryset.filter(pto_request_id=id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) 
def user_comments(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        comments = Comment.objects.filter(employee_id=request.employee.id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny]) 
def comments_detail(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)