from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Import models
from .models import AnimationContact
from .models import AnimationStand
from .models import AnimationActivity
from .models import AnimationPrestation

# Class base views
class ContactList(ListView):
    model = AnimationContact
    context_object_name = 'Contacts'
    template_name = 'Suivi/contactList.html'

# Create class view
class ContactCreate(CreateView):
    model = AnimationContact
    context_object_name = 'Contact'
    fields = '__all__'
    template_name = 'Suivi/contactForm.html'
    success_url = reverse_lazy('contactList')
class StandCreate(CreateView):
    model = AnimationStand
    context_object_name = 'Stand'
    fields = '__all__'
    template_name = 'Suivi/standForm.html'
    #success_url = reverse_lazy('') => update view
class ActivityCreate(CreateView):
    model = AnimationActivity
    context_object_name = 'Activity'
    fields = '__all__'
    template_name = 'Suivi/activityForm.html'
    #success_url = reverse_lazy('') => update view
class PrestaCreate(CreateView):
    model = AnimationPrestation
    context_object_name = 'Presta'
    fields = '__all__'
    template_name = 'Suivi/prestaForm.html'
    #success_url = reverse_lazy('') => update view

#Update class view
class ContactUpdate(UpdateView):
    model = AnimationContact
    fields = '__all__'
    template_name = 'Suivi/contactForm.html'
class StandUpdate(UpdateView):
    model = AnimationStand
    fields = '__all__'
    template_name = 'Suivi/standForm.html'
class ActivityUpdate(UpdateView):
    model = AnimationActivity
    fields = '__all__'
    template_name = 'Suivi/activityForm.html'
class PrestaUpdate(UpdateView):
    model = AnimationPrestation
    fields = '__all__'
    template_name = 'Suivi/prestaForm.html'

#Delete class view =>
class ContactDelete(DeleteView):
    model = AnimationContact
    context_object_name = 'Contact'
    template_name = 'Suivi/contactDelete.html'
    #success_url = reverse_lazy('') => update view
class StandDelete(DeleteView):
    model = AnimationStand
    context_object_name = 'Stand'
    template_name = 'Suivi/standDelete.html'
    #success_url = reverse_lazy('') => update view
class ActivityDelete(DeleteView):
    model = AnimationActivity
    context_object_name = 'Activity'
    template_name = 'Suivi/activityDelete.html'
    #success_url = reverse_lazy('') => update view
class PrestaDelete(DeleteView):
    model = AnimationPrestation
    context_object_name = 'Presta'
    template_name = 'Suivi/prestaDelete.html'
    #success_url = reverse_lazy('') => update view



# Function base views
def intraHome(request):
    return render(request, 'Suivi/intraHome.html')
