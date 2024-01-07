from django.urls import path
from .views import intraHome, ContactList

urlpatterns = [
    path('', intraHome, name='intraHome'),
    path('contactList/', ContactList.as_view(), name = 'contactList'),

]

#C:\Users\nicoh\Documents\Computer_science\Portfolio\Nanuq\Nanuq\Nanuq\static
#C:\Users\nicoh\Documents\Computer_science\Portfolio\Nanuq\Nanuq\static