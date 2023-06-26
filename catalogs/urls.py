from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.listings, name='listings'),
    path('retrievelist/<int:pk>/', views.listing_retrieve, name='retrievelist'),
    path('createlist/', views.listing_create, name ='createlist'),
    path('retrievelist/<int:pk>/edit/', views.listing_update, name='updatelist'),
    path('retrivelist/<int:pk>/delete/', views.listing_delete, name='deletelist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
