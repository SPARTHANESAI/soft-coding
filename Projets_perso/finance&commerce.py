import numpy as np 
rng = np.random.default_rng()
# Génération du tableau de données aléatoires comprises entre 500 et 6000 euro dans une format 12 x 31
ventes = rng.uniform(500, 6000, size = (12, 31))
# Insertion  de donn"es nan pour les jours inexistants
ventes[[3, 5, 8, 10], 30] = np.nan
ventes[1, 28:] = np.nan
# Filtrage de donn"es et remplaçement des nan par 0
ventes_filtrees = np.where(np.isnan(ventes), 0, ventes)
# Total des ventes pour ch acun des 12 mois
total_ventes_par_mois = np.sum(ventes_filtrees, 1)
# Moyenne des ventes quotidiennes pour chaque mois
moyenne_dailysales_par_mois = np.mean(ventes_filtrees, 1)
# Nombre de jours exact dans l'année où le chiffre d'affaire a depassé 5000 euro
jours_de_gloire = np.size(ventes_filtrees[ventes_filtrees  >= 5000])
# Extraire une sous matrice contenant uniquement les colonnes des weekends
jours = np.arange(31)
masque = (jours % 7 == 5) | (jours % 7 == 6)
weekends_sales = ventes_filtrees[:, masque]

print(f"Tableau initial de ventes : \n{ventes}")
print(f"Tableau contenant les zeros au lieu de nan : \n{ventes_filtrees}")
print(f"Total ses ventes par mois : \n{total_ventes_par_mois}")
print(f"Moyenne des ventes quotidiennes pour chaque mois : \n{moyenne_dailysales_par_mois}")
print(f"Nombre de jour de gloire : \n{jours_de_gloire}")
print(f"Ventes des weekends uniquement : \n{weekends_sales}")
