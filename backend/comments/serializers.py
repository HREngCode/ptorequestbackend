from rest_framework import serializers
from .models import Comment




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'pto_request', 'pto_request_id', 'employee', 'employee_id']
        depth = 0

        pto_request_id = serializers.IntegerField(write_only=True)
        employee_id = serializers.IntegerField(write_only=True)