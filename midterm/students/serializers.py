from rest_framework import serializers
from .models import StudentsData

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        # the model to be serialized
        model = StudentsData 
        # include all the fields from the student data
        fields = '__all__'