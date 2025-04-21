from django.shortcuts import render
from .models import StudentProfile, ProfileAttachments
def Student_list(request):
    students = StudentProfile.objects.all()
    for student in students:
        att = ProfileAttachments.objects.filter(student_id = student.pk)
        student.att = att
    return render(request, 'students/student_list.html',{'students':students})
def Student_detail(request, sid): 
    student = StudentProfile.objects.get(pk=sid)
    images = ProfileAttachments.objects.filter(student_id = student.pk)
    return render(request, 'students/details_page.html', {'student': student, 'images':images})
