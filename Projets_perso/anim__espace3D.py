import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

"""fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-3, 3, 3)
y = np.linspace(-3, 3, 3)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
surface = ax.plot_surface(X, Y, Z, cmap="viridis")
fig.colorbar(surface)
plt.show()"""

# initialisation de notre vue 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')

# initialisation de rng et creation de trois axes contenant des coordonées aléatoires
rng = np.random.default_rng()
x = rng.random(500)
y = rng.random(500)
z = rng.random(500)

# Afficher le titre de notre vue et placer x, y et z sur chacune des axes cocorrespondants
ax.set_title("Nuage de points 3D")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Afficher la les points avec scatter et definir la barre de couleur
sc = ax.scatter(x, y, z, c=z,  cmap="viridis", s=20, label="Differents points")
color_bar = plt.colorbar(sc)
color_bar.set_ticks([0.2, 0.5, 0.8])
color_bar.set_ticklabels(["Faible", "Moyen", "Elevé"])
# afficher les legendes (les labels)
ax.legend()


# definition de la fontion de mise  à jour
def update(frame): 
    ax.view_init(elev=30, azim=frame)
# Animation 
ani = FuncAnimation(fig, update, frames=range(0, 360, 2), interval=16)

# Afficher la vue elle-même
plt.show()
