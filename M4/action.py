from donnees import *

## syntaxe d'un algorithme de tri avec la clé de tri "lambda" qui a une propriété "temps"
def trier_donnees():
    poulss.sort(key=lambda x: x.temps)

##Afficher les données dans l’ordre du fichier .csv
def afficher_donnees():
    for donnee in poulss :
        print(donnee)

## Recherche et affichage des données pour un temps particulier
def rechercher_donnee(temps):
    for donnee in poulss:
        if donnee.temps == temps:
            return donnee
    return None

## Affichage des données en ordre croissant selon le temps
def trier_donnees_par_temps():
    poulss.sort(key=lambda x: x.temps) ## lambda est une clé de tri qui utilise la propriété "temps"
    for donnee in poulss:
        print(donnee.pouls, donnee.temps)

## Affichage des données en ordre croissant selon le pouls
def trier_donnees_par_pouls():
    poulss.sort(key=lambda x: x.pouls)  ## lambda est une clé de tri qui utilise la propriété "pouls"
    for donnee in poulss:
        print(donnee.pouls, donnee.temps)

##  Affichage des données en ordre décroissant selon le temps
def trier_donnees_par_temps_decroissant():
    poulss.sort(key=lambda x: x.temps,reverse=True) ## "reverse=true" est utilisée pour effectuer un tri en mode décroissant
    for donnee in poulss:
        print(donnee.pouls, donnee.temps)

##  Affichage des données en ordre décroissant selon le pouls
def trier_donnees_par_pouls_decroissant():
    poulss.sort(key=lambda x: x.pouls, reverse=True)
    for donnee in poulss:
        print(donnee.pouls, donnee.temps)

## Recherche et affichage des données pour un temps particulier
def rechercher_donnees_par_temps():
    temps_recherche = int(input("Entrez le temps : "))
    for donnee in poulss:
        if donnee.temps == temps_recherche:
            print(f"Temps : {donnee.temps} ,Pouls : {donnee.pouls}")
            return
    print("Aucune donnée trouvée pour ce temps.")

## Affichage de la moyenne de pouls dans une plage de temps donnée
def calculer_moyenne_pouls():
    plage_temps_debut = int(input("Entrez la plage de temps du debut : "))
    plage_temps_fin = int(input("Entrez la plage de temps de fin : "))
    pouls_total = 0
    nombre_donnees = 0
    for donnee in poulss:
        if donnee.temps >= plage_temps_debut and donnee.temps <= plage_temps_fin:
            pouls_total += donnee.pouls
            nombre_donnees += 1
    if nombre_donnees == 0:
        print("Aucune donnée trouvée pour cette plage de temps.")
    else:
        moyenne_pouls = pouls_total / nombre_donnees
        print(f"Moyenne de pouls pour la plage de temps [{plage_temps_debut},{plage_temps_fin}] : {moyenne_pouls}")

## Affichage du nombre de lignes de données actuellement en mémoire
def afficher_nombre_donnees():
    print(f"Nombre de données en mémoire : {len(poulss)}")

## Recherche et affichage des max/min de pouls (avec le temps associé)
def rechercher_pouls_max_min():
    if len(poulss) == 0:
        print("Aucune donnée en mémoire.")
        return
    pouls_max = poulss[0].pouls
    temps_pouls_max = poulss[0].temps
    pouls_min = poulss[0].pouls
    temps_pouls_min = poulss[0].temps
    for donnee in poulss:
        if donnee.pouls > pouls_max:
            pouls_max = donnee.pouls
            temps_pouls_max = donnee.temps
        if donnee.pouls < pouls_min:
            pouls_min = donnee.pouls
            temps_pouls_min = donnee.temps
    print(f"Pouls max : {pouls_max} (temps : {temps_pouls_max})")
    print(f"Pouls min : {pouls_min} (temps : {temps_pouls_min})")