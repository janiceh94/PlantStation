from django.shortcuts import render
from django.views.generic.base import TemplateView
 
class Landing(TemplateView):
   template_name = 'landing.html'
 
class Plant:
   def __init__(self, name):
       self.name = name
 
plants = [
   Plant('Monstera'),
   Plant('Alocasia'),
]
class Plant_List(TemplateView):
   template_name = 'plant_list.html'
 
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['plants'] = plants
       return context
