from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher

# LIST
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# ADD
def student_add(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            roll_number=request.POST.get('roll_number'),
            email=request.POST.get('email'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            student_class=request.POST.get('student_class')
        )
        return redirect('student_list')
    return render(request, 'student_form.html')

# DETAIL
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})

# EDIT / UPDATE
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.roll_number = request.POST.get('roll_number')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.student_class = request.POST.get('student_class')
        student.save()
        return redirect('student_list')
    return render(request, 'student_edit.html', {'student': student})

# DELETE
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_delete.html', {'student': student})



#List 
def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers_list.html', {'teachers': teachers})


#ADD
#   # Add Teacher
# def student_add(request):  
#     if request.method == "POST":
#         Teacher.objects.create(
#             name=request.POST.get('name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             gender=request.POST.get('gender'),
#             subjects=request.POST.get('subject'),  # or subject if renamed
#             salary=request.POST.get('salary')
#         )
#         return redirect('teacher_list')
#     teachers=Teacher.objects.all()
    