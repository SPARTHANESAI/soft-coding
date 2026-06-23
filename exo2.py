import numpy as np 

A = np.array([
    [1,2,3],
    [4,5,6]
])
B = np.array([10,20,30])
C = np.array([100,200])
D = 1000

print(A+B)
#print(A+C)
print(A+D)
# L'opération A + C ne marchera jamais et sortira toujours une erreur.

"""
    -----------NOTES--------------
    Numpy nous permet de gagner véritablement du temps dans les calculs.
    
    SOMME MATRICIELLE
    L'opération de somme ou de soustraction entre deux matrices d'entiers ou de reels est possible si et seulement si les deux matrices en 
    ont la même forme ou encore taille.
    
    Numpy permet aussi de faire la somme ou la soustraction entre une matrice d'estiers ou de reels et un nombre quelconque
    (entier, float...) donc on peut techniquement faire :
    Soit A une matrice quelconque
    Print(A + 10) ou  print(A - 32.2)
    
    NB: La somme entre une matrice d'entiers ou de réels et une matrice de chaînes de caractères est aussi possible 
    mais en fait numpy fait une concaténation et la matrice obtenue est de type String.
    
    
    PRODUIT MATRICIEL
    Soit un array A 
    Avec numpy, on peut faire très rapidement faire Ax2, ce qui serait probablement un peu plus long avec pythin simple
    Exemple 1 : Sans numpy 
        result = []
        for x in [1, 2, 3]:
            result.append(x*2)
    Il nous faut donc une boucle qui va tourner plusieurs fois et n'oublions pas aussi qu'en python simple les 
    élements d'une liste sont dispersés en mémoire, donc perd en vitesse.
    
    Exemple 2 : Avec Numpy
        result = np.array([1, 2, 3])
        result = result*2
        
    
    Le produit de deux matrices d'entiers ou de reels n'est possible que lorsque les deux matrices ont la même taille ou lorsque le nombre de
    colonnes de la première matrice est égal au nombre de lignes de la seconde. 
    Exemple : 
    Soient deux matrices A et B:
    A =   [4, 8, 2]          forme (2, 3)
          [9, 7, 0]

    B = [10, 25, 31]         forme (3, 3)
        [12, 10, 56]
        [0,  12, 40]
        
    Dans ce cas ci, le produit A x B est possible. Mais celui B x A ne l'est pas car le nombre de colonnes de B 
    n'est pas égal au nombre de lignes de A. 
    A x B = possible
    B x A = Impossible
    
    Le produit entre une matrice d'entiers ou de réels et une matrice composée de chaînes de caractères est aussi possible 
    mais au lieu d'une multiplication mathématiques, il se passe plutût une répétition ds chaînes de caractères.
    
    DIVISION MATRICIELLE

    La division entre deux matrices d'entiers ou de réels A et B est possible si et seulement si A ET B ont les mêmes tailles
    
"""