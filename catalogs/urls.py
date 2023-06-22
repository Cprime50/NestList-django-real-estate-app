from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from catalogs import views

from catalogs.views import listings , listing_retrieve, listing_create, listing_update, listing_delete,signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listings, name='listings'),
    path('listretrieve/<pk>/', views.listing_retrieve, name='list_retrieve'),
    path('add-listing/', views.listing_create, name ='listing_create'),
    path('listretrieve/<pk>/edit/', views.listing_update, name='listing_update'),
    path('listretrieve/<pk>/delete/', views.listing_delete, name='listing_delete'),
    path('signup/', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
