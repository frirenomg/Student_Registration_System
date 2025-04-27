from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentProfile, ProfileAttachments
from .form import Studentform
from django.contrib import messages
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

def addProfile(request):
    if request.method == 'POST':
        form = Studentform(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем основную информацию о студенте
            student = form.save()
            
            # Обрабатываем загруженные изображения
            if 'images' in request.FILES:
                images = request.FILES.getlist('images')
                for img in images:
                    ProfileAttachments.objects.create(
                        student=student,  # Используем связь OneToOneField
                        image=img
                    )
            return redirect('details_page', sid=student.pk)
    else:
        form = Studentform()
    
    return render(request, 'students/newprofile.html', {'form': form})

def editProfile(request, sid):
    # Получаем студента или возвращаем 404 если не найден
    student = get_object_or_404(StudentProfile, pk=sid)
    
    # Получаем текущие изображения профиля
    current_images = ProfileAttachments.objects.filter(student=student)
    
    if request.method == 'POST':
        form = Studentform(request.POST, request.FILES, instance=student)
        if form.is_valid():
            # Сохраняем изменения
            updated_student = form.save()
            
            # Обработка новых изображений
            if 'images' in request.FILES:
                # Удаляем старые изображения (если нужно)
                current_images.delete()
                
                # Добавляем новые изображения
                images = request.FILES.getlist('images')
                for img in images:
                    ProfileAttachments.objects.create(
                        student=updated_student,
                        image=img
                    )
            
            return redirect('details_page', sid=updated_student.pk)
    else:
        # Инициализируем форму с данными студента
        form = Studentform(instance=student)
    
    # Передаем текущие изображения в контекст
    context = {
        'form': form,
        'student': student,
        'current_images': current_images
    }
    
    return render(request, 'students/editprofile.html', context)

def deleteProfile(request, sid):
    student = get_object_or_404(StudentProfile, pk=sid)
    
    if request.method == 'POST':
        try:
            # Удаляем связанные изображения сначала
            ProfileAttachments.objects.filter(student=student).delete()
            # Затем удаляем самого студента
            student.delete()
            messages.success(request, 'Профиль студента успешно удален!')
            return redirect('student_list')
        except Exception as e:
            messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('details_page', sid=sid)
    
    # Если запрос GET - показываем подтверждение
    return render(request, 'students/confirm_delete.html', {'student': student})