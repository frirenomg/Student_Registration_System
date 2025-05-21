from django.db import models

class StudentProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('N', 'Не указан'),
    ]

    # Университетский ID студента
    student_id = models.CharField(max_length=20, unique=True, verbose_name="ID студента")
    iin = models.CharField(max_length=12, unique=True, verbose_name="ИИН")
    

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="Телефон")
    group = models.CharField(max_length=20, verbose_name="Группа")
    address = models.TextField(null=True, blank=True, verbose_name="Адрес")
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Активный'),
            ('graduate', 'Выпускник'),
            ('dismissed', 'Отчислен'),
            ('academic_leave', 'Академический отпуск'),
        ],
        default='active',
        verbose_name="Статус",
    )
    enrollment_date = models.DateField(verbose_name="Дата зачисления")
    graduation_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='N', verbose_name="Пол"
    )
    citizenship = models.CharField(max_length=50, null=True, blank=True, verbose_name="Гражданство")
    special_needs = models.TextField(null=True, blank=True, verbose_name="Особые потребности")

    class Meta:
        verbose_name = 'Профиль студента'
        verbose_name_plural = 'Профили студента'
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.group}) - ID: {self.student_id}"
    
class ProfileAttachments(models.Model):
    name = models.CharField(verbose_name='Название картинки', blank=True, null=True)
    image = models.FileField(upload_to='images', verbose_name='Файл')
    student = models.OneToOneField(StudentProfile, verbose_name=("Профиль студента"), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.image:
            file_name = self.image.name.split('.')[0].capitalize()
            self.name = file_name
        super().save(*args, **kwargs)
