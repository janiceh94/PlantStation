from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
   path('', views.Landing.as_view(), name='landing'),
   path('plants/', views.Plant_List.as_view(), name='plant_List'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)