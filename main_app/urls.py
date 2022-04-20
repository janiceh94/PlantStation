from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
    path('', views.Landing.as_view(), name='landing'),
    path('plants/', views.Plant_List.as_view(), name='plant_List'),
    # plant CRUD
    path('plants/new/', views.Plant_Create.as_view(), name='plant_create'),
    path('plants/<int:pk>/', views.Plant_Detail.as_view(), name='plant_detail'),
    path('plants/<int:pk>/update', views.Plant_Update.as_view(), name='plant_update'),
    path('plants/<int:pk>/delete', views.Plant_Delete.as_view(), name='plant_delete'),
    # user
    path('user/<username>/', views.profile, name='profile'),
    #soil 
    path('soil/', views.Soil_List, name='soil_list'),
    # soil CRUD
    # path('soil/new/', views.Soil_Create.as_view(), name='soil_create'),
    path('soil/<int:pk>/', views.Soil_Detail, name='soil_detail'),
    # path('soil/<int:pk>/update', views.Soil_Update.as_view(), name='soil_update'),
    # path('soil/<int:pk>/delete', views.Soil_Delete.as_view(), name='soil_delete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)