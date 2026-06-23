import numpy as np 
import matplotlib.pyplot as plt 

#---------Simulation de vol et télémétrie Drone------------
t = np.linspace(0, 10, 500)

x = np.cos(2*np.pi*t)
y = np.sin(2*np.pi*t)
z = 0.5*t**2

trajectoire = np.column_stack((x, y, z))
print(trajectoire.shape)
print(trajectoire)

delta_p = np.diff(trajectoire, axis = 0)
delta_t = np.diff(t)
print(delta_p.shape)
print(delta_t.shape)
delta_v = delta_p / delta_t[:,np.newaxis]
print(delta_v.shape)
norme_delta_v = np.sqrt(np.sum(delta_v**2, axis = 1))

print(norme_delta_v)

indice_seuil_depasse = np.where(norme_delta_v > 11)[0]
print(indice_seuil_depasse)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(projection = '3d')
ax.plot(trajectoire[:, 0], trajectoire[:, 1], trajectoire[:, 2], color="blue", linewidth = 2, label="vol du drone" )
if len(indice_seuil_depasse) > 0:
    ax.scatter(trajectoire[indice_seuil_depasse, 0], trajectoire[indice_seuil_depasse, 1], trajectoire[indice_seuil_depasse, 2], color='red', s=20, label="Alerte : vitesse > 11 m/s")
ax.set_title("Télémétrie 3D - Evolution du drone en spirale")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")
ax.legend()
plt.show()