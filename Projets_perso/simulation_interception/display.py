import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from config import  CARTE_X_MAX, CARTE_Y_MAX, CARTE_Z_MAX
from engine import executer_simulation

def dessiner_dome(ax, centre, rayon, couleur):
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi/2, 15)
    
    x = rayon * np.outer(np.cos(u), np.sin(v))+ centre[0]
    y = rayon * np.outer(np.sin(u), np.cos(v))+ centre[1]
    z = rayon * np.outer(np.ones_like(u), np.cos(v))+ centre[2]
    
    ax.plot_surface(x, y, z, color=couleur, alpha=0.10, edgecolor=couleur, linewidth=0.3)
def lancer_interface():
        # 1. Récupération des calculs du moteur
        donnees = executer_simulation()
        hist_avion = donnees["historique_avion"]
        hist_missile = donnees["historique_missile"]
        t_interception = donnees["temps_interception"]
        t_detection = donnees["temps_detection"]
        
        # 2. Configuration de la scène 3D
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        fig.canvas.manager.set_window_title("Systtème Radar et interception 3D")
        
        # 3. Dessin des dômes Radar
        dessiner_dome(ax, donnees["base_A"].position, donnees["base_A"].rayon_influence, donnees["base_A"].couleur)
        dessiner_dome(ax, donnees["base_B"].position, donnees["base_B"].rayon_influence, donnees["base_B"].couleur)
        
        # Dessin des bases (carrés au sol)
        ax.scatter(*donnees["base_A"].position, color='blue', marker='s', s=200, label='Base A')
        ax.scatter(*donnees["base_B"].position, color='red', marker='s', s=200, label='Base B')
        
        # 4. Initialisation des trçés mobiles
        ligne_avion, = ax.plot([], [], [], color='gold', lw=2.5, label="Trajectoire Avion")
        ligne_missile, = ax.plot([], [], [], color='lime', linestyle='--', lw=1.5, label="Trajectoire Missilze")
        point_avion = ax.scatter([], [], [], color='black', marker='^', s=100)
        point_missile = ax.scatter([], [], [], color='crimson', marker='o', s=50)
        texte_status = ax.text2D(0.02, 0.93, "", transform=ax.transAxes, fontsize=11, 
                                 weight='bold', bbox= dict(facecolor='white', alpha= 0.8,  edgecolor='gray'))
        
        # Ajustement des axes 
        ax.set_xlim(0, CARTE_X_MAX)
        ax.set_ylim(0, CARTE_Y_MAX)
        ax.set_zlim(0, CARTE_Z_MAX)
        ax.set_xlabel('X (km)')
        ax.set_ylabel('Y (km)')
        ax.set_zlabel('Z  Altitude(km)')
        ax.set_title("Simulation de défense aérienne 3D", fontsize=12, weight="bold")
        ax.legend(loc='upper right')
        
        # 5. Fonction d'animation frame par frame
        def animer (frame):
            limite = frame +1
            if t_interception != -1 and frame > t_interception : 
                limite = t_interception + 1
            # Avion 
            ligne_avion.set_data(hist_avion[:limite, 0], hist_avion[:limite, 1] )
            ligne_avion.set_3d_properties(hist_avion[:limite, 2])
            if limite > 0:
                point_avion._offsets3D = ([hist_avion[limite-1, 0], hist_avion[limite-1, 1], hist_avion[limite-1, 2],])
            
            # Missile 
            ligne_missile.set_data(hist_missile[:limite, 0], hist_missile[:limite, 1] )
            ligne_missile.set_3d_properties(hist_missile[:limite, 2])
            if limite > 0:
                point_missile._offsets3D = ([hist_missile[limite-1, 0], hist_missile[limite-1, 1], hist_missile[limite-1, 2],])
            
            # Onfographie dynamique (statut textus)
            
            if t_detection == -1 or frame < t_detection:
                texte_status.set_text(f"TEMPS : {frame}s\nSTATUT : Vol de l'avion (Intrus)\nRADAR : RAS")
                texte_status.get_bbox_patch().set_edgecolor('gray')
            elif frame >= t_detection and (t_interception == -1 or frame < t_interception):
                texte_status.set_text(f"TEMPS : {frame}s\nSTATUT : VIOLATION ESPACE AERIEN\nMISSILE : En poursuite...")
                texte_status.get_bbox_patch().set_edgecolor('red')
            elif  t_interception != -1 and frame >= t_interception:
                texte_status.set_text(f"TEMPS : {frame}s\nSTATUT : INTERCEPTION REUSSIE\nCible détruite.")
                texte_status.get_bbox_patch().set_edgecolor('green')
            return ligne_avion, point_avion, ligne_missile, point_missile
        nb_frames = t_interception + 10 if t_interception != -1 else len(hist_avion)
        global ani
        ani = animation.FuncAnimation(fig, animer, frames=nb_frames, interval=50, blit = False, repeat=False)
        
        plt.show()
        
if __name__ == "__main__":
    lancer_interface()
                
        
                
            
        
        
        
        
    
    