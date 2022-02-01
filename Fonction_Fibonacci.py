#!/usr/bin/env python
# coding: utf-8

# In[1]:


# c) Fonction suite de Fibonacci

def Fibonacci():
    '''
    Prend en entrée un argument n et affiche la suite de Fibonacci

    Paramètre:
            n : un entier

    Sortie:
            La suite de Fibonacci en fonction de n
    '''
    n = int(input("Entrez un nombre: "))
    n1 = 0 
    n2 = 1
    compteur = 0

    if n <= 0:
        print("Veuillez choisir un nombre entier supérieur à 0")
    elif n == 1:
        print("Les deux premiers termes sont", n1, "et", n)
    else:
        print("La suite Fibonacci est:")
        while compteur < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            compteur = compteur + 1


# In[2]:


Fibonacci()

