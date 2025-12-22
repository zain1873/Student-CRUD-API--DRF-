from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializers = EmployeeSerializer(employees, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    # post
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # single emplyee record 

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return(employee)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # put method
    def put(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete method
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

