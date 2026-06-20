from django.shortcuts import render, redirect
from .models import Client, Commande, Livraison

def dashboard(request):
    context = {
        'clients_count': Client.objects.count(),
        'commandes_count': Commande.objects.count(),
        'livraisons_count': Livraison.objects.count(),
    }

    return render(request, 'delivery/dashboard.html', context)


def clients(request):
    recherche = request.GET.get('recherche')

    if recherche:
        clients = Client.objects.filter(nom__icontains=recherche)
    else:
        clients = Client.objects.all()

    return render(
        request,
        'delivery/clients.html',
        {
            'clients': clients
        }
    )

def ajouter_client(request):
    if request.method == 'POST':

        nom = request.POST['nom']
        telephone = request.POST['telephone']
        adresse = request.POST['adresse']

        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        Client.objects.create(
            nom=nom,
            telephone=telephone,
            adresse=adresse,
            latitude=latitude if latitude else None,
            longitude=longitude if longitude else None
        )

        return redirect('clients')

    return render(request, 'delivery/ajouter_client.html')
def supprimer_client(request, id):
    client = Client.objects.get(id=id)
    client.delete()

    return redirect('clients')
def modifier_client(request, id):
    client = Client.objects.get(id=id)

    if request.method == 'POST':
        client.nom = request.POST['nom']
        client.telephone = request.POST['telephone']
        client.adresse = request.POST['adresse']

        client.save()

        return redirect('clients')

    return render(
        request,
        'delivery/modifier_client.html',
        {'client': client}
    )
def commandes(request):
    commandes = Commande.objects.all()

    return render(
        request,
        'delivery/commandes.html',
        {
            'commandes': commandes
        }
    )
def ajouter_commande(request):

    if request.method == 'POST':

        client_id = request.POST['client']
        produit = request.POST['produit']
        quantite = request.POST['quantite']
        date_commande = request.POST['date_commande']

        client = Client.objects.get(id=client_id)

        Commande.objects.create(
            client=client,
            produit=produit,
            quantite=quantite,
            date_commande=date_commande
        )

        return redirect('commandes')

    clients = Client.objects.all()

    return render(
        request,
        'delivery/ajouter_commande.html',
        {'clients': clients}
    )

def livraisons(request):
    livraisons = Livraison.objects.all()

    return render(
        request,
        'delivery/livraisons.html',
        {
            'livraisons': livraisons
        }
    )
def ajouter_livraison(request):

    if request.method == 'POST':

        commande_id = request.POST['commande']
        statut = request.POST['statut']
        date_livraison = request.POST['date_livraison']

        commande = Commande.objects.get(id=commande_id)

        Livraison.objects.create(
    commande=commande,
    statut=statut,
    date_livraison=date_livraison
)

        return redirect('livraisons')

    commandes = Commande.objects.all()

    return render(
        request,
        'delivery/ajouter_livraison.html',
        {'commandes': commandes}
    )
def modifier_livraison(request, id):

    livraison = Livraison.objects.get(id=id)

    if request.method == 'POST':

        livraison.statut = request.POST['statut']
        livraison.save()

        return redirect('livraisons')

    return render(
        request,
        'delivery/modifier_livraison.html',
        {'livraison': livraison}
    )
def supprimer_livraison(request, id):
    livraison = Livraison.objects.get(id=id)
    livraison.delete()
    return redirect('livraisons')
def carte(request):

    recherche = request.GET.get('recherche')

    client = None

    if recherche:
        client = Client.objects.filter(
            nom__icontains=recherche
        ).first()

    return render(
        request,
        'delivery/carte.html',
        {
            'client': client
        }
    )