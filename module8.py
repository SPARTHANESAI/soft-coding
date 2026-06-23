import numpy as np

"""
    EXERCICE : MANIPULATION AVANCEE DE DONNEES (Fancy Indexing et np.argsort)
    Différents capteurs mesurent différents signaux
"""
capteurs_id = np.array(["capteur_A", "capteur_B", "capteurs_C", "capteur_D", "capteur_E"])
signaux = np.array([14.2, 5.1, 19.5, 2.3, 11.0])

# Essayons de recupérer par leurs index les ID des capteurs 1, 3 et 4 en utilisant le fancy indexing
capteurs_index = capteurs_id[[1, 3, 4]]
print(capteurs_index)

# Trions le tableau signaux à l'aide de np.argsort (ça fait le tri suivant l'index des valeurs)
indices_tri = np.argsort(signaux)
print(indices_tri)

# Transposons mtn ces index triés dans capteurs_ID pour essayer d'obtenir aussi les capteurs 
# triés dans l'ordre selon leurs performances
capteurs_ordre = capteurs_id[indices_tri]
print("capteurs par ordre de performance :", capteurs_ordre)
