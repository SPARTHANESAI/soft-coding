
#------------Exercice 1 Numpy-------------------

import numpy   as np;
data = np.array([[1,2], [3,6], [5,6]])
data = data.reshape(2,3)
"""print(*[type(data), 
        data.shape, 
        data.ndim, 
        data.size, 
        data.dtype, 
        data.sum(), 
        data.mean()],
      sep='\n')"""
def describe(x):
    print(
        f"Data : \n{x}\n"
        f"Type : {type(x)}\n"
        f"Shape : {x.shape}\n"
        f"Ndims :  {x.ndim}\n"
        f"Size : {x.size}\n"
        f"Dtype : {x.dtype}\n"
        f"Sum : {x.sum()}\n"
        f"Mean : {x.mean()}\n"
    )
describe (data);


""""
    -----NOTES-------
    L'objet array prend deux arguments : (données, type de données)
    Exemple : np.array([1,2,3,4], dtype = int64)
    Le deuxième argument est optionnel. C'est pourquoi sans notre exercice nous ne l'avaons pas spécifié.
    
    Avec numpy, les différentes listes passées comme données dans l'objet array doivent 
    contenir le même nombre d'élements, et doivent être homogènes (C'est-à-dire
    de même type). 
    
    Aussi il est important de savoir que les tableaux array avec numpy sont différents
    des listes classiques python qont les élements sont stockés de manière dispersée en méloire. 
    Les array numpy stockent leurs contenus côte à côte en mémoire (Ce qui o^timise encore plus les 
    manipulations sur ces données).
    
    De plus numpy est codé dans le langage C qui est un langage bas niveau, donc très proche de la 
    machine, reconnu pour Sa rapidité dans l'exécution
"""