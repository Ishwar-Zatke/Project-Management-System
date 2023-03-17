from django.db import models

# Create your models here.


class DataStudent(models.Model):
    student_name=models.CharField(max_length=100) 
    student_email=models.CharField(max_length=100) 
    student_address=models.CharField(max_length=150) 
    student_mobile=models.BigIntegerField(max_length=12,default=0)
    student_project_type=models.CharField(max_length=10)
    student_project_name=models.CharField(max_length=100)
    student_project_code=models.IntegerField()
    student_project_fees=models.IntegerField()
    student_project_payment_mode =models.CharField(max_length=30, default="Online")
    student_date_of_payment=models.DateField()