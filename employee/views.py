from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from .paginations import CustomPagination
from .filters import EmployeeFilter
from rest_framework.filters import SearchFilter

# Create your views here.

class Employees(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    filterset_class = EmployeeFilter
    search_fields = ['emp_name']

    # post
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # single emplyee record 

class EmployeeDetail(APIView):
    def get(self,request,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # put method
    def put(self,request,pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete method
    def delete(self,request,pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


