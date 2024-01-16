from django.urls import path
from .views import intraHome
from .views import ContactList, ContactCreate, ContactUpdate
from .views import StandCreate, StandUpdate
from .views import ActivityCreate, ActivityUpdate
from .views import PrestaCreate, PrestaUpdate

urlpatterns = [
    path('', intraHome, name='intraHome'),
    path('contactList/', ContactList.as_view(), name = 'contactList'),
    path('contactCreate/', ContactCreate.as_view(), name = 'contactCreate'),
    path('standCreate/', StandCreate.as_view(), name = 'standCreate'),
    path('activityCreate/', ActivityCreate.as_view(), name = 'activityCreate'),
    path('prestaCreate/', PrestaCreate.as_view(), name = 'prestaCreate'),
    path('contactUpdate/', ContactUpdate.as_view(), name = 'contactUpdate'),
    path('standUpdate/', StandUpdate.as_view(), name = 'standUpdate'),
    path('activityUpdate/', ActivityUpdate.as_view(), name = 'activityUpdate'),
    path('prestaUpdate/', PrestaUpdate.as_view(), name = 'prestaUpdate'),
]

#C:\Users\nicoh\Documents\Computer_science\Portfolio\Nanuq\Nanuq\Nanuq\static
#C:\Users\nicoh\Documents\Computer_science\Portfolio\Nanuq\Nanuq\static