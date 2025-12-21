from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializers = EmployeeSerializer(employees, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    # post
    def post(self, request):
        serializers = EmployeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
