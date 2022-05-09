from django import forms

from ouakki_ayoub.models import Produit

from ouakki_ayoub.models import Commande

from ouakki_ayoub.models import Categorie

from ouakki_ayoub.models import Personne


class produitF(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"


class CommandeF(forms.ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"


class PersonneForm(forms.ModelForm):
    class Meta:
        model:Personne
        fields="__all__"
