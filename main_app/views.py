from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Plant
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
 
class Landing(TemplateView):
   template_name = 'landing.html'

class Plant_List(TemplateView):
   template_name = 'plant_list.html'
 
   def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get('name')
    if name != None:
        context['plants'] = Plant.objects.filter(name__icontains=name)
        context['header'] = f'Searching for {name}'
    else:
        context['plants'] = Plant.objects.all()
        context['header'] = 'All Plants: '
    return context

# plant CRUD
class Plant_Create(CreateView):
    model = Plant
    fields = ['name', 'img', 'water', 'light', 'temperature']
    template_name = 'plant_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/plants/')

class Plant_Detail(DetailView):
    model = Plant
    template_name = 'plant_detail.html'

class Plant_Update(UpdateView):
    model = Plant
    fields = ['name', 'img', 'water', 'light', 'temperature']
    template_name = 'plant_update.html'
    
    def get_success_url(self):
        return reverse('plant_detail', kwargs={'pk': self.object.pk})

class Plant_Delete(DeleteView):
    model = Plant
    template_name = 'plant_delete.html'
    success_url='/plants/'

def profile(request, username):
    user = User.objects.get(username=username)
    plants = Plant.objects.filter(user=user)
    return render(request, 'profile.html', {'username':username, 'plants': plants})
    