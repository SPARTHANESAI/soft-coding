import numpy as np 

def calculer_distance(point_1, point_2): 
    """
        Calcule la distance géométrique réelle entre deux points 3D (X, Y, Z)
        Formule : sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
    """
    return np.linalg.norm(point_1 - point_2)

def obtenir_vecteur_direction(origine, cible):
    
    """
        calcule le vecteur unitaire (de longueur 1) pointant de l'origine vers la cible
        Très essentiel pour orienter le déplacemnt de l'avion et le guidage du missile
    """
    vecteur = cible - origine
    norme = np.linalg.norm(vecteur)
    if norme == 0 : 
        return np.array([0.0, 0.0, 0.0])
    return vecteur/norme
    