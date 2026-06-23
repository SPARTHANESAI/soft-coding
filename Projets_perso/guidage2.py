import numpy   as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation as fa 
# Variation du temps
dt = 0.1
# Positioin initiale et vitesse de l'avion
avion_pos = np.array([0.0, 0.0]) ; avion_vitesse = np.array([4.5, 17.5])

# Position initiale et vitesse du missile

missile_pos = np.array([175, 0.0]) ; missile_vitesse = 20.0
fig, ax = plt.subplots()
line_avion, = ax.plot([], [], 'ro', color='blue', label="Avion")
line_missile, = ax.plot([], [], 'bo', color='red', label="Missile")
line2_missile, = ax.plot([], [], '--', color='red', linewidth=0.5, markersize=2)
ax.set_title("Interception d'avion par un missile", weight='bold')
ax.set_xlabel("X (m)") ; ax.set_ylabel("Y (m)")
ax.legend()
ax.set_xlim(-10 , 200) ; ax.set_ylim(-10, 200)
running = True
seuil_capture = 0.2
x_missile = []
y_missile = []
def update(i):
    global avion_pos, avion_vitesse, missile_pos, missile_vitesse, dt, running, ani, x_missile, y_missile
    if not running : return line_avion, line_missile
    avion_pos = avion_pos + avion_vitesse*dt
    line_avion.set_data([avion_pos[0]], [avion_pos[1]])
    
    if i > 20 :
        missile_direction = avion_pos - missile_pos
        distance = np.linalg.norm(missile_direction)
        if distance < seuil_capture : 
            print("Cible atteint")
            running = False
            ani.event_source.stop()
        else:
            missile_pos = missile_pos +  (missile_direction/distance)*missile_vitesse*dt
        #line_avion.set_data([avion_pos[0]], [avion_pos[1]])
        line_missile.set_data([missile_pos[0]], [missile_pos[1]])

        

        x_missile.append(missile_pos[0])
        y_missile.append(missile_pos[1])
        line2_missile.set_data([x_missile[:i]], [y_missile[:i]])
    current_xmax = ax.get_xlim()[1]
    current_ymax = ax.get_ylim()[1]
    max_xobjet = max(avion_pos[0], missile_pos[0])
    max_yobjet = max(avion_pos[1], missile_pos[1])
    if max_xobjet > current_xmax - 50 :
        ax.set_xlim(-20, max_xobjet + 50)
    if max_yobjet > current_ymax - 50 :
        ax.set_ylim(-20, max_yobjet + 50)
    
ani = fa(fig, update, frames=2000, interval=16)
plt.show()