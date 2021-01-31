from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    skills = models.CharField(max_length=30)
    
    def __str__(self):
        my_teacher = self.teacher_id + "" + self.first_name
        return my_teacher


