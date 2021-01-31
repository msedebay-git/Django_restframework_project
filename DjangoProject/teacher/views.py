from django.shortcuts import render

# Create your views here.
from .models import Teacher
from .serializer import TeacherSerializers
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


class TeacherAPI(APIView):
    
    def get(self, request):
        all_teacher = Teacher.objects.all()
        output = TeacherSerializers(all_teacher, many=True)
        return Response(output.data)
    
    
    def post(self, request):
        teacher_data = JSONParser().parse(request)
        input_teacher = TeacherSerializers(data = teacher_data)
        if input_teacher.is_valid():
            print("teacher data received and valid")
            input_teacher.saved()
            return JsonResponse(input_teacher.data, status.HTTP_201_CREATED)
        return JsonResponse(input_teacher.errors, status.HTTP_400_BAD_REQUEST)
    
    
        



