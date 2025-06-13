from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # URL для формы смены языка ДОЛЖЕН быть вне i18n_patterns
    path('i18n/', include('django.conf.urls.i18n')),
]

# Мультиязычные маршруты
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    prefix_default_language=False  # Важно для работы без префикса языка по умолчанию
)

# Статика и медиа в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)