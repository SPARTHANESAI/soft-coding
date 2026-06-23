import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 

#------- ZSPACE SYMPY ---------------

#Déclaration de la variable symbolique 
x = sp.symbols('x')
# Définition de la fontion 
f = x**3 + 3*x**2 + 2
# Dérivée exacte 
f_prime = sp.diff(f, x)
#Recherche des points critiques
points_critiques = sp.solve(f_prime)

print("fonction f(x) =", f )
print("Dérivée f'(x) =", f_prime)
print("Points critiques :", points_critiques)

# Affichons mathématiquement les points critiques 
for p in points_critiques : 
    print(f"f({p}) =", f.subs(x, p))
    
#----------------ESPACE NUMPY------------------

f_num = sp.lambdify(x, f, modules="numpy")
f_prime_num = sp.lambdify(x, f_prime, modules="numpy")
x = np.linspace(-3, 3, 600)

y = f_num(x)
y_prime = f_prime_num(x)

# ----------------ESPACE MATPLOTLIB -------------------

fig = plt.figure()
x_crit = np.array(points_critiques, dtype="float")
y_crit = f_num(x_crit)

plt.plot(x, y, label="f(x)=x³+3x²+2", color='blue')
plt.plot(x, y_prime, '--',label="f'(x)=3x²+6x", color='red')

plt.scatter(x_crit, y_crit, color='green', s=20, label='Points critiques')

for xc, yc in zip(x_crit, y_crit):
    plt.annotate(f'({xc:.0f}, {yc:.0f})',
                 (xc, yc),
                 xytext=(10,10),
                 textcoords='offset points')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.ylabel('y')
plt.title("Analyse de la fonction et de sa dérivée")
plt.legend()
plt.grid(True)

plt.show()