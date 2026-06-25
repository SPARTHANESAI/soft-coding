import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
from sympy.calculus.util import continuous_domain

# 3 D&finissons la variable symbolique "x"
x = sp.symbols('x')

# Définissons la fonction représentant le déplacement de l'avion 
f = (2-x**2 + 100 * x)/x

# Cherchons le domaine de définition de la fonction f(x)
df = continuous_domain(f,x, sp.S.Reals)

# Croisons ce domaine avec notre le domaine de test que nous avons choisi [0, 100]
our_domain_test = sp.Interval(0, 100)
final_domain = df.intersect(our_domain_test)

print(our_domain_test, final_domain)

# Calculons sa dérivée 
f_prime = sp.diff(f, x)

# Affichons la fonction, son domaine de définition  et sa dérivée 
print(f"Fonction f(x) = {f}")
print(f"Domaine de définition df = {df}")
print(f"Dérivée f'(x) = {f_prime}")

# Convertissons la fonction sympy en fonction numérique aves la méthode lamdify de sympy 
f_num = sp.lambdify(x, f, modules='numpy')
x = np.linspace(0, 100, 1000)
y = f_num(x)

# Organisons l'affichage avec matplotlib
plt.figure()
plt.title("Simulation interception d'avion ")
plt.xlabel('x en (km)')
plt.ylabel('y (altitude)')
plt.axhline(0, color='black')
plt.axvline(0, color="black")
# plt.xlim(-40, 40)
# plt.ylim(-40, 40)

plt.plot(x, y, color='red', label="Trajectoire de l'avion")
plt.legend()
plt.show()

"""
    SUITE DU TRAVAIL A FAIRE 
    
    1. Chercher a afficher correctement le domaine de définition en utilisant str.replace() dur final_domain.
    2. Chercher à convertir proprement le domaine de définition dans un tableau numpy linspace pou r le test.
    3. Afficher en étudions la ens de varitaion de la fonction, si l'avion monte ou descends (Pro :  Essayer de dynamiser l'affichage
    pour qu'au moment o l'avion monte on voit uniquement le texte signalant sa montée et qu'au moment où il descend on en voit 
    aussi le texte xorrespondant ). 
    4. Introduire le concept de vitesse de l'avion. 
    5. Introduire le missile et poursuivre la simulation jusqu'à la fin. 
"""


