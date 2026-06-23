import numpy    as np 
# Dimensions de l'espace de simulation (en km)

CARTE_X_MAX = 160.0
CARTE_Y_MAX = 160.0
CARTE_Z_MAX = 50.0

# Propriétés des infrastructures 
RAYON_INFLUENCE_A = 45.0   # Rayon du dôme bleu (km)
RAYON_INFLUENCE_B = 45.0   # Rayon du dôme Rouge (km)

# Position initiales au sol [X, Y, Z]
POS_BASE_A = np.array([30.0, 40.0, 0.0])
POS_BASE_B = np.array([120.0, 110.0, 0.0])

# Performances physiques (converties directement en km/s)
VITESSE_AVION = 0.250 # 250 m/s   --> 0.25 km/s
VITESSE_MISSILE = 0.600 # 600 m/s --> 0.60 km/s

# Paramètres temporels infrastructures
DT = 1.0   # Echantillonage de la simulation ( 1 seconde par itération)
TEMPS_MAX = 200