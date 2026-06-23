import numpy as np 
"""
    EXERCICE : Vectoriqation avancée et l'optimisation
"""
X = np.linspace(-5, 5, 10)
print(f"Tableau X : {X}")
# Appliquons la foncion à tout les elements de X
Y = np.sqrt(np.abs(X))
print(f"Tableau Y : {Y}")
# verifions s'il y a dans notre tableau la moindre valeur supérieure à 2.0 avec np.any()
print(f"Y'a-t-il une valeur supérieure à 2.0 ? : {np.any(Y > 2.0)}")
# Remplaçons toutes les valeurs du tableau qui sont supérieures à 2.0 par 2.0
print(f"Ecretage de signal : {np.where(Y > 2.0, 2.0, Y)}")