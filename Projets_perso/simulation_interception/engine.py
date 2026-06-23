import numpy as np 
from config import POS_BASE_A, POS_BASE_B, RAYON_INFLUENCE_A, TEMPS_MAX, VITESSE_MISSILE, DT
from math_utils import calculer_distance
from entities import Base, Avion, Missile 

def executer_simulation():
    # 1.Initialisation des infrastructures
    base_A = Base(nom="Base A (Bleue)", position=POS_BASE_A, rayon_influence=RAYON_INFLUENCE_A, couleur="blue")
    base_B = Base(nom="Base B (Rouge)", position=POS_BASE_B, rayon_influence=45.0, couleur="red")
    # 2; Initialisation des mobiles
    # L'avion décolle de B. On lui donne une cible fictive pourqu'il traverse A
    point_cible_avion = POS_BASE_A + np.array([-20.0, 30.0, 15.0]) # Trajectoire en digonale ascendante
    
    avion = Avion(base_B.position, point_cible_avion)
    # Le missile attend patiemment sur la base A
    missile = Missile(base_A.position)
    
    # 3. Variables d'état du système
    detected = False
    temps_detection = -1
    temps_interception = -15
    log_evenements = []
    
    # 4. Boucle de simulation temporelle
    for t in range(TEMPS_MAX):
        avion.avancer()
        if not detected:
            distance_base_A = calculer_distance(avion.position, base_A.position)
            if distance_base_A <= base_A.rayon_influence:
                detected = True
                temps_detection = t
                missile.lance = True # Ordre de tir envoyé au missile
                log_evenements.append(f"[{t}s] Alerte : Violation espace arien base A detectée")
        # Mise à jour du missile (s'il est lancé, il trque; sinon il reste au sol)
        missile.poursuivre(avion.position)
            
        # Condition d'interception (Succès)
        if detected and avion.en_vie:
            distance_missile_avion = calculer_distance(missile.position, avion.position)
                
            # Si le missile est assez proche pour impacter pendant ce pas de temps (dt)
            if distance_missile_avion <= (VITESSE_MISSILE*DT):
                avion.en_vie = False
                temps_interception = t
                log_evenements.append(f"[{t}] SUCCES : Avion intercepté et détruit par le missile")
                break # On arrête les calculs physiques. L'interception a deja eu lieu
    # On retourne un dictionnaire completcontenant toutes les données calculées
    return {
        "base_A":base_A,
        "base_B":base_B,
        "historique_avion":np.array(avion.historique_positions),
        "historique_missile":np.array(missile.historique_positions),
        "detected": detected, 
        "temps_detection":temps_detection,
        "temps_interception": temps_interception,
        "logs": log_evenements                      
            }
    
# Petit test rapide pour vérifier que les données fonctionnent en taches de fond
if __name__ == "__main__":
    print("lancement d'un calcul test...")
    resultats = executer_simulation()
    for log in resultats["logs"]:
        print(log)
    