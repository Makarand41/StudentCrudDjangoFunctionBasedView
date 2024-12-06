from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from app01.forms import StudentForm
from app01.models import Student



def getStudents(request):
    students = Student.objects.all()  # Corrected method call syntax
    return render(request, 'index.html', {'students': students})  # Corrected dictionary syntax for context


def createStudent(request):
    form = StudentForm()  # Initialize the form
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the home page or relevant URL
    return render(request, 'create.html', {'form': form})  # Use dictionary for context

def deleteStudent(request, id):
    student = get_object_or_404(Student, id=id)  # Use get_object_or_404 for safety
    student.delete()
    return redirect('/')  # Correct the redirect path


def updateStudent(request, id):
    student = get_object_or_404(Student, id=id)  # Use get_object_or_404 for error handling
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update.html', {'form': form, 'student': student})

def logout_view(request):
    return render(request, 'logout.html')
