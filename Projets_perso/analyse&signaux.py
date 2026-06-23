import numpy as np  
import matplotlib.pyplot as plt 

#--------------Création & Analyse de signaux ECG (ElectroCardiogramme)------------
rng = np.random.default_rng()
# Génération d'un tableau initial ne contenant que de base (0)
signaux = np.zeros(1000)
# Définition de pics à intervalles réguliers dans ce tableau (1.0)
signaux[::150] = 1.0
# Simulation de petits bruits ou ondes parasites autours de la valeur de base 0 dans ce tableau
bruits = rng.normal(0, 0.1, 1000)
ECG_brut = signaux + bruits
# Normalisons mtn notre ECG_brut avec une formule statistique pour obtenir de la cohérence (vrai ECG)
ECG = (ECG_brut - np.min(ECG_brut))/(np.max(ECG_brut - np.min(ECG_brut)))
# Récupérons les indices des battements du coeur (Posons: pic = battement de coeur si pic >= 0.7)
mask_booleen = ECG >= 0.7
indices_pics = np.where(mask_booleen)[0]
# Cherchons les intervalles entres battements de coeur et calculons leur moyenne
indices_filtrees = indices_pics[indices_pics > 10]
intervalles = np.diff(indices_filtrees)
intervalle_moyen = np.mean(intervalles)
# Appliquons mtn la formule de calcul du pouls des (battements de coeur par minute BPM)
BPM = (60*100)/intervalle_moyen
plt.plot(ECG)
plt.text(400, 1.1, f"ECG en cours d'analyse...       Pouls = {BPM} BPM ", ha = 'center')
plt.show()


