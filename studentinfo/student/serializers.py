from rest_framework import serializers
from .models import StudentData

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentData
        # fields = ('first_name', 'last_name')
        fields = '__all__'
