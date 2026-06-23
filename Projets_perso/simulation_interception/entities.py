import numpy as np 
from config import VITESSE_AVION, VITESSE_MISSILE, DT
from math_utils import calculer_distance, obtenir_vecteur_direction

class Base: 
    def __init__(self, nom, position, rayon_influence, couleur):
        self.nom = nom
        self.position = position
        self.rayon_influence = rayon_influence
        self.couleur = couleur   # utile pour l"affichage (bleu ou rouge)

class Avion:
    def __init__(self, position_initiale, position_cible):
        self.position = np.array(position_initiale, dtype=float)
        self.historique_positions = [np.copy(self.position)]
        self.en_vie = True
        self.direction = obtenir_vecteur_direction(self.position, np.array(position_cible))
        
    def avancer(self):
        if not self.en_vie :  return
        self.position += self.direction + VITESSE_AVION*DT
        self.historique_positions.append(np.copy(self.position))
        
class Missile:
    def __init__(self, position_initiale):
        self.position = np.array(position_initiale, dtype = float)
        self.historique_positions = [np.copy(self.position)]
        self.lance = False
    
    def poursuivre(self, position_actuelle_avion):
        if not self.lance : 
            self.historique_positions.append(np.copy(self.position))
            return
        direction_vers_avion = obtenir_vecteur_direction(self.position, position_actuelle_avion)
        self.position += direction_vers_avion*VITESSE_MISSILE*DT
        self.historique_positions.append(np.copy(self.position))