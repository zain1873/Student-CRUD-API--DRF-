from rest_framework import serializers
from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    emp_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'


