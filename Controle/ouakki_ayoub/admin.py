from django.contrib import admin

# Register your models here.

from .models import Produit
from .models import Categorie
from .models import Commande
from .models import Personne

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Commande)
admin.site.register(Personne)

