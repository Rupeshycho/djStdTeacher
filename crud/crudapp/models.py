from django.db import models

# ---------- Student Model ----------
class Student(models.Model):
    # Student basic info
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        )
    )
    student_class = models.CharField(
        max_length=10,
        choices=(
            ('ONE','Class 1'),
            ('TWO','Class 2'),
            ('THREE','Class 3'),
            ('FOUR','Class 4'),
            ('FIVE','Class 5'),
            ('SIX','Class 6'),
            ('SEVEN','Class 7'),
            ('EIGHT','Class 8'),
            ('NINE','Class 9'),
            ('TEN','Class 10'),
        )
    )
    
    # Photo upload
    photo = models.FileField(upload_to='student_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

# ---------- Teacher Model ----------
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        )
    )
    subjects = models.CharField(
        max_length=50,
        choices=(
            ('MATH', 'Mathematics'),
            ('SCI', 'Science'),
            ('ENG', 'English'),
            ('NEP', 'Nepali'),
            ('SOC', 'Social Studies'),
            ('ECO', 'Economics'),
        )
    )
    salary = models.IntegerField()
    # Photo upload
    photo = models.FileField(upload_to='teacher_photos/', null=True, blank=True)
    # Auto added join date
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name