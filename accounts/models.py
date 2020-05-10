from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # is_student = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default=False)
    is_govt = models.BooleanField(default=False)
    is_FPS = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  
#     sapid = models.CharField(max_length=200, default='SOME STRING')
    
#     def __str__(self):
#         return self.user.username