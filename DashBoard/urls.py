
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobseeker/', include('jobseeker.urls')),
    path('employer/', include('employer.urls')),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
