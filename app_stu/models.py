from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length = 10)
    student_fname = models.CharField(max_length = 50)
    student_lname = models.CharField(max_length = 50)
    mark = models.IntegerField()
    mail_id = models.EmailField() 
    contact = models.IntegerField()
    class Meta:
        db_table = 'std_table'
