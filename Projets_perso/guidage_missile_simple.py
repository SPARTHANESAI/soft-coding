import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation as Fa 

dt = 0.1
dtm = 0.1
avion_pos = np.array([0.0, 0.0])
avion_vit = np.array([0.5, 0.4])
missile_pos = np.array([20.0, -25.0])
missile_vit = 1.0

SEUIL_CAPTURE = 0.0
fig, ax = plt.subplots()
ax.set_xlim(-5, 2000)
ax.set_ylim(-5, 2000)
avion_plot, = ax.plot([], [], 'ro', label="Avion")
missile_plot, = ax.plot([], [], 'bo',label= 'Missile')
ax.legend()

running = True
def update(i):
    global avion_pos, missile_pos, running
    if not running : return  avion_plot,  missile_plot
    avion_pos = avion_pos + avion_vit*dt
    direction_missile = avion_pos - missile_pos
    distance = np.linalg.norm(direction_missile)
    if distance < SEUIL_CAPTURE :
        print("Cible atteinte")
        running = False
    else:
        direction_missile = direction_missile/distance
        missile_pos = missile_pos + direction_missile*missile_vit*dtm
    avion_plot.set_data([avion_pos[0]], [avion_pos[1]])
    missile_plot.set_data([missile_pos[0]], [missile_pos[1]])
    ax.set_xlim(min(avion_pos[0], missile_pos[0])-20, max(avion_pos[0], missile_pos[0])+20)
    ax.set_ylim(max(avion_pos[1], missile_pos[1])-20, max(avion_pos[1], missile_pos[1])+20)       
  
    
    
ani = Fa(fig, update, frames=2000, interval=16, blit=False, repeat = False)
plt.show()