from django.shortcuts import render

# Create your views here.

def intraHome(request):
    return render(request, 'Suivi/intraHome.html')
