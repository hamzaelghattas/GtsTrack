from django.contrib import admin
from .models import Client, Commande, Livraison

admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Livraison)


