import csv
import time
import random

# Définition des constantes
DUREE_PRELEVEMENT = 30 * 60  # Durée de la prise de pouls en secondes
FREQUENCE_CARDIAQUE = 70  # Fréquence cardiaque moyenne en bpm
PRELEVEMENT_INTERVAL = 30  # Intervalle entre chaque prélevement en secondes
MAX_PRELEVEMENTS = 30  # Nombre maximum de prélevements

# Génération des données
donnees = []
prelevements = 0
debut = time.time()  # Heure de début de la prise de pouls
while prelevements < MAX_PRELEVEMENTS and time.time() - debut < DUREE_PRELEVEMENT:
    temps = int((time.time() - debut) * 1000)
    pouls = random.randint(FREQUENCE_CARDIAQUE - 5, FREQUENCE_CARDIAQUE + 5)
    donnees.append((temps, pouls))
    prelevements += 1
    time.sleep(PRELEVEMENT_INTERVAL)

# Stockage des données dans un fichier CSV
with open('Battemens.csv', mode='w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Temps (ms)', 'Pouls (bpm)'])  # Écriture de l'en-tête
    for temps, pouls in donnees:
        writer.writerow([temps, pouls])
