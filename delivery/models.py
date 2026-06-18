from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()

    def __str__(self):
        return self.nom


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.CharField(max_length=100)
    quantite = models.IntegerField()
    date_commande = models.DateField()

    def __str__(self):
        return self.produit


class Livraison(models.Model):
    STATUTS = [
        ('En attente', 'En attente'),
        ('En préparation', 'En préparation'),
        ('En livraison', 'En livraison'),
        ('Livré', 'Livré'),
    ]

    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=STATUTS)
    date_livraison = models.DateField()

    def __str__(self):
        return self.statut