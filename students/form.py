from django import forms
from .models import StudentProfile

from django import forms

class SingleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = False  # запрещаем выбор нескольких файлов

class SingleFileField(forms.FileField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs.setdefault('widget', SingleFileInput)  # ставим новый виджет
        kwargs.setdefault('required', False)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        return super().clean(data, initial)  # обычная очистка одного файла

class Studentform(forms.ModelForm):
    images = SingleFileField()
    class Meta:
        model = StudentProfile
        fields = (
            'student_id', 'iin', 'first_name', 'last_name', 'date_of_birth',
            'email', 'phone_number', 'group', 'address', 'status',
            'enrollment_date', 'graduation_date', 'gender', 'citizenship', 'special_needs', 'images'
        )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
            'graduation_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 2}),
            'special_needs': forms.Textarea(attrs={'rows': 2}),
            'gender': forms.Select(choices=StudentProfile.GENDER_CHOICES),
            'status': forms.Select(choices=StudentProfile._meta.get_field('status').choices),
        }
        labels = {
            'student_id': 'ID студента',
            'iin': 'ИИН (Индивидуальный идентификационный номер)',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'date_of_birth': 'Дата рождения',
            'email': 'Электронная почта',
            'phone_number': 'Телефон',
            'group': 'Группа',
            'address': 'Адрес проживания',
            'status': 'Статус студента',
            'enrollment_date': 'Дата зачисления',
            'graduation_date': 'Дата окончания',
            'gender': 'Пол',
            'citizenship': 'Гражданство',
            'special_needs': 'Особые потребности',
        }