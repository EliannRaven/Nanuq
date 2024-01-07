from django.shortcuts import render
from django.views.generic.list import ListView

#Import models
from .models import AnimationContact

# Class base views

class ContactList(ListView):
    model = AnimationContact
    context_object_name = 'Contacts'
    template_name = 'Suivi/contactList.html'




# Function base views

def intraHome(request):
    return render(request, 'Suivi/intraHome.html')
