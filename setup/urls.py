from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from setup import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imoveis.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)