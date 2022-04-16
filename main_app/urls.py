from django.urls import path
from . import views
 
urlpatterns = [
   path('', views.Landing.as_view(), name='landing'),
   path('plants/', views.Plant_List.as_view(), name='plant_List'),
]
