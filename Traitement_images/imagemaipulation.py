import numpy as np 
import matplotlib.pyplot as plt 

image = np.array([
    [
        [255, 0, 0],
        [0, 255, 0]
    ],
    [
        [0, 0, 255],
        [255, 255, 0]
    ]
])

image2 =  image[1, 1, :].copy()
print(f"Récupérons dans une vue les éléments indexés : {image2}")
image2[2] = 255
print(f"Affichons notre vue modifiée : {image2}")
print(f"Etat du tableau initial après opération : \n{image}")
# Modifions mtn directement le tableau initial et vérifions l'état de la vue image2
image[1, 1, 2] = 0
print(f"Etat de la vue après opération : {image2}")