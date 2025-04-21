from django.contrib import admin
from .models import StudentProfile, ProfileAttachments
admin.site.register(ProfileAttachments)
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Основная информация", {
            'fields': ('student_id', 'iin', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'group')
        }),
        ("Дополнительная информация", {
            'fields': ('address', 'status', 'enrollment_date', 'graduation_date', 'gender', 'citizenship', 'special_needs'),
            'classes': ('collapse',),  # Свернуть эту секцию по умолчанию
        }),
    )
    list_display = ('student_id', 'first_name', 'last_name', 'group', 'status', 'email')  
    search_fields = ('student_id', 'first_name', 'last_name', 'email')  
    list_filter = ('group',)  # Фильтрация
