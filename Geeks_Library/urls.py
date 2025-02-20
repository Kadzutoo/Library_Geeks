from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('library.urls')),
    path('', include('hashtags.urls')),
    path('cart/', include('cart.urls')),
    path('', include('parser_kinogo.urls')),
    path('', include('recipes.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
