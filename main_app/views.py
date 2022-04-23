from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Plant, Soil
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
 
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
        context['header'] = 'All Plants'
    return context

# plant CRUD
class Plant_Create(LoginRequiredMixin, CreateView):
    model = Plant
    fields = '__all__'
    template_name = 'plant_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/plants/')

class Plant_Detail(DetailView):
    model = Plant
    template_name = 'plant_detail.html'

class Plant_Update(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = '__all__'
    template_name = 'plant_update.html'
    
    def get_success_url(self):
        return reverse('plant_detail', kwargs={'pk': self.object.pk})

class Plant_Delete(LoginRequiredMixin, DeleteView):
    model = Plant
    template_name = 'plant_delete.html'
    success_url='/plants/'

# User profile
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    plants = Plant.objects.filter(user=user)
    soils = Soil.objects.filter(user=user)
    return render(request, 'profile.html', {'username':username, 'plants': plants, 'soils': soils})
    
# soil CRUD
def Soil_List(request):
    soils = Soil.objects.all()
    return render(request, 'soil_list.html', {'soils': soils})

def Soil_Detail(request, soil_id):
    soil = Soil.objects.get(id=soil_id)
    return render(request, 'soil_detail.html', {'soil':soil})

class Soil_Create(LoginRequiredMixin, CreateView):
    model = Soil
    fields = '__all__'
    template_name = "soil_create.html"
    success_url = '/soil/'

class Soil_Update(LoginRequiredMixin, UpdateView):
    model = Soil
    fields = '__all__'
    template_name = "soil_update.html"
    success_url = '/soil/'

class Soil_Delete(LoginRequiredMixin, DeleteView):
    model = Soil
    template_name = 'soil_delete.html'
    success_url = '/soil/'

# auth
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            print('Hello', user.username)
            return HttpResponseRedirect('/user/' + str(user.username)+'/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})