import numpy as np 

"""
    EXERCICE : Le traitement de sdonnées manquantes NaN et l'infinité
    Voici les relevés de température d'un nouveau capteur sur 6 jours. Malheureusement, le capteur a eu de ratés
"""

releves = np.array([21.5, np.nan, 23.0, 24.5, np.nan, 22.0])

# calculons la moyenne avec np.mean sans tenir compte des NaN
print(releves.mean())
# Recalculons en utilisant la onfction NaN Safe np.nanmean
print(np.nanmean(releves))
# Détecteons où se trouvent les nan et remplaçons-les par 0.0 avec np.isnanet np.where
print(np.where(np.isnan(releves) ,0.0, releves) )
# Notes : isnan() retourne un tableau de booleen etdonc la ou c'est true ça remplace par 0 et laisse le reste