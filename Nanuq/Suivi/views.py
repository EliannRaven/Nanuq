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
    template_name = 'Suivi/contactCreate.html'
    #success_url = reverse_lazy('') => update view
class StandCreate(CreateView):
    model = AnimationStand
    context_object_name = 'Stand'
    fields = '__all__'
    template_name = 'Suivi/standCreate.html'
    #success_url = reverse_lazy('') => update view
class ActivityCreate(CreateView):
    model = AnimationActivity
    context_object_name = 'Activity'
    fields = '__all__'
    template_name = 'Suivi/activityCreate.html'
    #success_url = reverse_lazy('') => update view
class PrestaCreate(CreateView):
    model = AnimationPrestation
    context_object_name = 'Presta'
    fields = '__all__'
    template_name = 'Suivi/prestaCreate.html'
    #success_url = reverse_lazy('') => update view

#Update class view
class ContactUpdate(UpdateView):
    model = AnimationContact
    fields = '__all__'
    template_name = 'Suivi/contactUpdate.html'
class StandUpdate(UpdateView):
    model = AnimationStand
    fields = '__all__'
    template_name = 'Suivi/standUpdate.html'
class ActivityUpdate(UpdateView):
    model = AnimationActivity
    fields = '__all__'
    template_name = 'Suivi/activityUpdate.html'
class PrestaUpdate(UpdateView):
    model = AnimationPrestation
    fields = '__all__'
    template_name = 'Suivi/prestaUpdate.html'

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
