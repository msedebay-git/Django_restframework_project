'''
Created on Jan 30, 2021

@author: msedebay
'''
from rest_framework import serializers
from .models import Teacher


class TeacherSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ['teacher_id','first_name','last_name','skills']
