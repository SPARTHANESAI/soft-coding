import numpy as np 

V = np.array([
    [1, 2],
    [3, 4]
])
T = np.array([
    [0, -1],
    [1, 0]
])
# Faisons le produit matriciel T x V
V_transforme = T@V
print(V_transforme)
# Faisons la trnspositions de V_transforme
print(V_transforme.T) 
# Maintenant, essayons de générer un tablean de quatre éléments au hasard aveec randn
Bruit = np.random.randn(4)
print(Bruit)

