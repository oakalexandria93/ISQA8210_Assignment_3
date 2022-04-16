from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pet'

urlpatterns = [
        path('', views.pet_list, name='pet_list'),
        path('pet_list', views.pet_list, name='pet_list'),
        path('signup', views.signup, name='signup'),
        path('pet_detail', views.pet_detail, name='pet_detail'),
        path('pet/create/', views.pet_new, name='pet_new'),
        path('pet/<int:pk>/edit/', views.pet_edit, name='pet_edit'),
        path('pet/<int:pk>/delete/', views.pet_delete, name='pet_delete'),
        path('pet_post/<int:post_id>', views.pet_post, name='pet_post'),

              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
