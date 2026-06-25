import sympy as sp 
import numpy as np  
import matplotlib.pyplot as plt 
 
 # Définissons la fonction symbolique
x = sp.symbols('x')
f = (2*x**2 - 3)/(x-1)
f_prime = sp.diff(f, x)
points_critiques = sp.solve(f_prime, x, domain=sp.S.Reals)
# Convertissons les fonctions symboliques en fonctions numériques
f_num = sp.lambdify(x, f, modules='numpy')
f_prime_num = sp.lambdify(x, f_prime, modules='numpy')
# Séquençons les différentes valeurs pour respecter le domaine de définition de la fonction qui est x =! 1
x1 = np.linspace(-4, 1, 500, endpoint=False)
x2 = np.linspace(1, 4, 300)[1:]
x = np.concatenate((x1, x2))
# Trouvons les valeurs par chacune des fonctions des x 
y = f_num(x)
y_prime = f_prime_num(x)
# Récupérons les valeurs des points critiques et trouvons leurs images par  la fonction f
x_crit = np.array([ float(p) for p in points_critiques if p.is_real])
y_crit = f_num(x_crit)
# Initialisation matplotlib
plt.figure()
plt.plot(x, y, color='blue', label="f(x)=(2*x**2 - 3)/(x-1)")
plt.plot(x, y_prime, '--', color='red', label="f'(x)=4*x/(x - 1) - (2*x**2 - 3)/(x - 1)**2")
plt.scatter(x_crit, y_crit, s=20, label="Points critiques")
# Boucle pour afficher les coordonnées des points au dessus des points crtitiques
for xc, yc in zip(x_crit, y_crit):
    plt.annotate(f"f({xc:.0f}, {yc:0.fcat})", (xc, yc), xytext=(10, 10), textcoords='offset points')
# Mise en forme de l'interface graphique
plt.title("Analyse de la fonction f(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
# Traçons correctement les lignes repères en noir correctement
plt.axhline(0, color='black')
plt.axvline(0, color=('black'))
plt.axvline(1, color=('yellow'))

plt.ylim(-20, 20)
plt.show()