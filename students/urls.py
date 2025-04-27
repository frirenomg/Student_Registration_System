from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Student_list, Student_detail, addProfile, editProfile, deleteProfile

urlpatterns = [
    path('', Student_list, name='student_list'),
    path('<int:sid>/', Student_detail, name='details_page'),  # Заменили pid на sid
    path('add/', addProfile, name='add_profile'),
    path('edit/<int:sid>/', editProfile, name='edit_profile'),
    path('delete/<int:sid>/', deleteProfile, name='delete_profile'),
]

# Подключение медиа-файлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
