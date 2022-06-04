
from os import path


app_name = 'clients'

urlpatterns = [
    path('mobile/clients/',
         ClientsListCreate.as_view(), name='mobileClients'),
]