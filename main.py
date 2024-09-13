"""
Code pour trouver les nombres premier de 0 à 100
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Retourne si p est premier ou non.

    Args:
        p: valeur entiere positive
    """
    if p==0 :
        return False
    if p==1 :
        return False
    for i in range (2,int(sqrt(p)+1)):
        if p%i==0 :
            return False
    return True

#### Fonction principale


def main():
    """
    Appel de la fonction
    """
    for n in range(100):
        if isprime(n) is True:
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
