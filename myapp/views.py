# from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def StudentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializers = StudentSerializer(students, many=True)
        return Response(serializers.data,  status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,  status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)
    

# fetch only single student data

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    






