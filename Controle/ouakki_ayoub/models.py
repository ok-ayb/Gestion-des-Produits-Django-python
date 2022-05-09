from django.db import models


# Create your models here.

class Categorie(models.Model):
    id_Ca = models.IntegerField(primary_key=True)
    nomCategorie = models.CharField(max_length=20)


    def __str__(self):
        return self.nomCategorie

class Produit(models.Model):
    id = models.IntegerField(primary_key=True)
    refProduit = models.CharField(max_length=20)
    nomProduit = models.CharField(max_length=20)
    dateProduction = models.DateField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.FloatField()

    def __str__(self):
        return self.nomProduit

class Personne(models.Model):
    id_P = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    def __str__(self):
        return self.nom




class Commande(models.Model):
    id_Co = models.IntegerField(primary_key=True)
    referenceCmd = models.CharField(max_length=20)
    dateCmd = models.DateField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client=models.OneToOneField(Personne,on_delete=models.CASCADE)
    def __str__(self):
        return self.referenceCmd


