from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Plant
 
class Landing(TemplateView):
   template_name = 'landing.html'

class Plant_List(TemplateView):
   template_name = 'plant_list.html'
 
   def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get('name')
    if name != None:
        context['plants'] = Plant.objects.filter(name__icontains=name)
    else:
        context['plants'] = Plant.objects.all()
    return context

