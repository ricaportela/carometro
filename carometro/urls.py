from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve




urlpatterns = [
    path('media/', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static/', serve,{'document_root': settings.STATIC_ROOT}),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('photos/', include(('carometro.photos.urls','photos'), namespace='photos')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
