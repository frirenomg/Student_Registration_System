from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Student_list, Student_detail

urlpatterns = [
    path('', Student_list, name='student_list'),
    path('<int:sid>/', Student_detail, name='details_page'),  # Заменили pid на sid
]

# Подключение медиа-файлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
