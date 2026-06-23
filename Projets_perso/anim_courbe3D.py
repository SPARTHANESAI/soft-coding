import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation as fa 
"""
    ---------- ANIMATION COURBE 2D -------------
    
    Une animation est une boucle qui fait trois choses :
    1. dessiner une courbe vide
    2. ajouter des points petit à petit
    3. raffraîchir l'écran
    1 image = 1 frame
"""
# Créeons une ligne vide ou interface vide
fig, ax = plt.subplots()
line, = ax.plot([], []) # "line," ne recupère pas le retour de la fonction mais plutot l'objet ax.plot() lui même
# fixons les limites de l'interface pour qu'a chaque raffraichissement ça ne change
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# initialisons les fonctions et definissons le tableau indicateur du temps
t = np.linspace(0, 10, 1000)
x = np.sin(t)
y = np.cos(t)

# Définissons la fonction de mise à jour
def update(i):
    # Insérons à chque frame les points à afficher
    line.set_data(x[:i], y[:i])
    return line, 

ani = fa(fig, update, frames= len(t),  interval= 16) #"frames" = nombre d'images au total,  "interval = temps en millisecond
plt.show()