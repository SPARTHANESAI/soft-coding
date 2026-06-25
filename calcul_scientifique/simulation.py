import sympy as sp 
# import numpy as np 
# import matplotlib.pyplot as plt 

x = sp.symbols('x')
f = 2*x**3 + x**2 + 3
print("Soit la fonction f(x) représentant la trajectoire de l'avion. f(x) = ", f, "\n")


# calculons la dérivée première f'(x)
f_prime = sp.diff(f, x)
print(f"Dérivée première f'(x) = {f_prime}\n")

# solvons l'équation f'(x) = 0

points_critiques = sp.solve(f_prime, x)
print(f"Les points critiques sont : { points_critiques}\n")

# Affichons les valeurs de par f(x) de chacun des ces points critiques
print("Image par f(x) de chacun des points critiques :")
for i in points_critiques : 
    print(f"f({i}) = {f.subs(x, i)}    ", end="")


# vérifions si ces deux points critiques sont des maximum ou minimum locaux, Pour cela étudioins la dérivée seconde 

f_prime_prime = sp.diff(f_prime)
print(f"\n\nDérivée seconde f''(x) = {f_prime_prime}\n")

for i in points_critiques: 
    val_par_f_prime =  f_prime_prime.subs(x, i)
    nature = ("minimum local" if val_par_f_prime > 0 else " maximum local" if val_par_f_prime < 0 else "Comportement non pris en charge")
    print(f"f''({i}) = {val_par_f_prime} --> {nature}")
    
# Etudions maintenant le sens de variation de la fonction déterminnons les intervalles 

f_prime = sp.factor(f_prime)
# Affichonsla dérivée factorisée
print(f"\n f'(x) factorisée --> {f_prime}")
intervalle_monte = sp.solve_univariate_inequality(f_prime > 0, x)
intervalle_descente = sp.solve_univariate_inequality(f_prime < 0, x)

print("\nSENS DE VARIATION DE LA FONCTION f(x)")
print(f"Sur l'intervalle {intervalle_monte}, l'avion monte")
print(f"Sur l'intervalle {intervalle_descente}, l'avion descend")