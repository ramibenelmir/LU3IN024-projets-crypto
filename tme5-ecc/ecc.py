# Sorbonne Université LU3IN024 2021-2022
# TME 5 : Cryptographie à base de courbes elliptiques
#
# Etudiant.e 1 : NOURA ALJANE 28600768
# Etudiant.e 2 : RAMI BENELMIR 21221977

from math import *
import matplotlib.pyplot as plt
from random import randint

# Fonctions utiles

def exp(a, N, p):
    """Renvoie a**N % p par exponentiation rapide."""
    def binaire(N):
        L = list()
        while (N > 0):
            L.append(N % 2)
            N = N // 2
        L.reverse()
        return L
    res = 1
    for Ni in binaire(N):
        res = (res * res) % p
        if (Ni == 1):
            res = (res * a) % p
    return res


def factor(n):
    """ Return the list of couples (p, a_p) where p is a prime divisor of n and
    a_p is the p-adic valuation of n. """
    def factor_gen(n):
        j = 2
        while n > 1:
            for i in range(j, int(sqrt(n)) + 1):
                if n % i == 0:
                    n //= i
                    j = i
                    yield i
                    break
            else:
                if n > 1:
                    yield n
                    break

    factors_with_multiplicity = list(factor_gen(n))
    factors_set = set(factors_with_multiplicity)

    return [(p, factors_with_multiplicity.count(p)) for p in factors_set]


def inv_mod(x, p):
    """Renvoie l'inverse de x modulo p."""




    return exp(x, p-2, p)


def racine_carree(a, p):
    """Renvoie une racine carrée de a mod p si p = 3 mod 4."""
    assert p % 4 == 3, "erreur: p != 3 mod 4"

    return exp(a, (p + 1) // 4, p)


# Fonctions demandées dans le TME

def est_elliptique(E):
    """
    Renvoie True si la courbe E est elliptique et False sinon.

    E : un triplet (p, a, b) représentant la courbe d'équation
    y^2 = x^3 + ax + b sur F_p, p > 3
    """
    p , a , b = E
    delta = ( (4 * (a**3)) +( 27 * (b ** 2)) ) % p
    if delta == 0 : return False
    return True 


def point_sur_courbe(P, E):
    """Renvoie True si le point P appartient à la courbe E et False sinon."""
    if P == () : 
        return True

    p , a , b = E
    x , y = P

    y_1 = pow(y,2) % p 
    y_2 = (pow(x,3) + (a * x) + b) % p
    
    if y_1 == y_2 : return True 

    return False


def symbole_legendre(a, p):
    """Renvoie le symbole de Legendre de a mod p."""
    
    return exp ( a , (p-1) // 2 , p ) # on utilise la fonction exp qui nous permet de calculer :  a puissance (p-1) // 2 dans Z/pZ



def cardinal(E):
    """Renvoie le cardinal du groupe de points de la courbe E."""
    p, a, b = E
    cpt = 1 # l'infini
    for x in range(p):
            z = (x**3 + x * a + b) % p  #eviter la foction pow 

            legendre = symbole_legendre(z, p)
            
            if legendre == 1: cpt += 2           
            
            elif legendre == 0: cpt += 1
    #print(cpt)
    return cpt


def liste_points(E):
    """Renvoie la liste des points de la courbe elliptique E."""
    p, a, b = E

    assert p % 4 == 3, "erreur: p n'est pas congru à 3 mod 4."

    liste_points = [()]
    
    for x in range(p):

        z = (x ** 3 + a * x + b) % p
        legendre = symbole_legendre(z, p)
        
        if legendre == 0: 
            
            liste_points.append((x, 0))
        
        elif legendre == 1:

            y = racine_carree(z, p)
            
            liste_points.append((x, y))
            liste_points.append((x, -y))

    return liste_points


def cardinaux_courbes(p):   # faut ajouter le theoreme de hasse
    """
    Renvoie la distribution des cardinaux des courbes elliptiques définies sur F_p.

    Renvoie un dictionnaire D où D[i] contient le nombre de courbes elliptiques
    de cardinal i sur F_p.
    """
    D = {}

    for b in range(p):
       
        for a in range(p):
            E = p, a, b
            
            if est_elliptique(E): 
               
                card = cardinal(E)
                if card in D :
                    D[card] += 1
                else:
                    D[card] = 1
    return D


    
    
    return D


def dessine_graphe(p):
    """Dessine le graphe de répartition des cardinaux des courbes elliptiques définies sur F_p."""
    bound = int(2 * sqrt(p))
    C = [c for c in range(p + 1 - bound, p + 1 + bound + 1)]
    D = cardinaux_courbes(p)

    plt.bar(C, [D[c] for c in C], color='b')
    plt.show()


def moins(P, p):
    """Retourne l'opposé du point P mod p."""
    #if P == () : return ()

    x, y = P
    return x % p, -y % p


def est_egal(P1, P2, p):
    """Teste l'égalité de deux points mod p."""
    if P1 == P2 == () : 
        #print("je suis la 1")
        return True

    elif  ( P1 == () )  or ( P2 == () ) : 
        #print("je suis la 2")

        return False 
    else :
        x1, y1 = P1
        x2, y2 = P2
        
        if x1 % p == x2 % p and y1 % p == y2 % p: 
            return True
        
    return False


def est_zero(P):
    """Teste si un point est égal au point à l'infini."""
    if P == () : return True
    return False


def addition(P1, P2, E):
    """Renvoie P1 + P2 sur la courbe E."""
    p, a, b = E

    if est_zero(P1): return P2
    elif est_zero(P2): return P1
    
    elif est_egal(P1, moins(P2, p), p) or est_egal(moins(P1,p),P2, p):  return ()

    x1, y1 = P1
    x2, y2 = P2

    if est_egal(P1, P2, p):
        
        R = ((3 * (x1 ** 2)+ a) * inv_mod(2 * y1, p)) % p
    
    else: 
        
        R = ((y2 - y1) * inv_mod(x2 - x1, p)) % p

    x = (R ** 2 - x1 - x2) % p
    y = (R * (x1 - x) - y1) % p

    if point_sur_courbe((x, y), E):  return x, y

    return ()



def multiplication_scalaire(k, P, E):
    """Renvoie la multiplication scalaire k*P sur la courbe E."""
    
    return


def ordre(N, factors_N, P, E):
    """Renvoie l'ordre du point P dans les points de la courbe E mod p. 
    N est le nombre de points de E sur Fp.
    factors_N est la factorisation de N en produit de facteurs premiers."""

    return 


def point_aleatoire_naif(E):
    """Renvoie un point aléatoire (différent du point à l'infini) sur la courbe E."""
    
    return 


def point_aleatoire(E):
    """Renvoie un point aléatoire (différent du point à l'infini) sur la courbe E."""

    return


def point_ordre(E, N, factors_N, n):
    """Renvoie un point aléatoire d'ordre N sur la courbe E.
    Ne vérifie pas que n divise N."""

    return

def keygen_DH(P, E, n):
    """Génère une clé publique et une clé privée pour un échange Diffie-Hellman.
    P est un point d'ordre n sur la courbe E.
    """
    sec = None # A remplacer
    pub = None # A remplacer
    
    return (sec, pub)

def echange_DH(sec_A, pub_B, E):
    """Renvoie la clé commune à l'issue d'un échange Diffie-Hellman.
    sec_A est l'entier secret d'Alice et pub_b est l'entier public de Bob."""

    return
