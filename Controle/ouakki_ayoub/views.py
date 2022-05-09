from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import request
from ouakki_ayoub.models import *
from ouakki_ayoub.models import Categorie
from ouakki_ayoub.models import Commande
from .forms import *
from ouakki_ayoub.models import *

from .models import Produit


def index(request):
    resultsdisplay = Produit.objects.all()
    p = Paginator(resultsdisplay, 10)
    page = request.GET.get('page')
    prd = p.get_page(page)

    return render(request, 'index.html', {'Produit': prd})


def search_Product(request):
    if request.method == "POST":
        searched = request.POST['search']
        produits = Produit.objects.filter(
            Q(nomProduit__contains=searched) | Q(refProduit__contains=searched) | Q(id__contains=searched))

    return render(request, 'searchProduct.html', {'searched': searched, 'produits': produits})


def commandParPersonne(request):
    if request.method == "POST":
        searchedC = request.POST['searchC']
        personnes = Commande.objects.filter(client=searchedC)

        return render(request, 'commandeParPersonne.html', {'searchedC': searchedC, 'personnes': personnes})


def detail(request, id):
    commandes=None
    try:
        context = Produit.objects.get(id=id)
        commandes = Commande.objects.get(id_Co=id)
        var = 1
    except Commande.DoesNotExist  :
         var = 0
    return render(request, 'detail.html', {'commandes': commandes, 'context': context, 'var': var})


def prodF(request):
    if request.method == "POST":
        form = produitF(request.POST).save()
        return redirect('/ouakki_ayoub')
    else:
        form = produitF
    return render(request, 'formP.html', {'form': form})


def CmdF(request):
    if request.method == "POST":
        form = CommandeF(request.POST).save()
        messages.success(request, 'l ajoute du commande est bien effectuer')
        return redirect('/ouakki_ayoub')
    else:
        form = CommandeF
    return render(request, 'formCo.html', {'form': form})


def CatF(request):
    if request.method == "POST":
        form = CategorieForm(request.POST).save()
        return redirect('/ouakki_ayoub')
    else:
        form = CategorieForm
    return render(request, 'formCa.html', {'form': form})


