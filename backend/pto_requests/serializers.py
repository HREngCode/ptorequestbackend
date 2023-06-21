from rest_framework import serializers
from .models import PtoRequest

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class PtoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PtoRequest
        fields = ['id', 'employee_id', 'employee', 'date_requested', 'hours_requested', 'approved']
        depth = 1

    employee_id = serializers.IntegerField(write_only=True)