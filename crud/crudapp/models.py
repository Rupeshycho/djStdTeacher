from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    STUDENT_CLASS = [
        ('ONE', 'Class 1'),
        ('TWO', 'Class 2'),
        ('THREE', 'Class 3'),
        ('FOUR', 'Class 4'),
        ('FIVE', 'Class 5'),
        ('SIX', 'Class 6'),
        ('SEVEN', 'Class 7'),
        ('EIGHT', 'Class 8'),
        ('NINE', 'Class 9'),
        ('TEN', 'Class 10'),
    ]

    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    student_class = models.CharField(
        max_length=10,
        choices=STUDENT_CLASS,
        default='ONE'
    )

    def __str__(self):
        return f"{self.name} -  {self.get.student_class_display()}"
    
    
    
class Teacher(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others '),
    ]
    SUBJECTS=[
        ('MATH','Mathematics'),
        ('SCI','Science'),
        ('ENG','English'),
        ('NEP','Nepali'),
        ('SOC','Social Studies '),
        ('ECO','Economics'),
    ]
    
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15, unique =True)
    gender=models.CharField(max_length=1,choices = GENDER_CHOICES) 
    subjects=models.CharField(max_length=10, choices=SUBJECTS)
    
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    date_joined=models.DateField(auto_now_add= True )

    def __str__(self):
        return f"{self.name} - {self.get_subjects_display()}"   
    