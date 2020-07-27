from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.home, name='home'),
    path('<int:blog_id>/', shop.views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
