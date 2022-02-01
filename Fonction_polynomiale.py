#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a) Fonction polynomiale

def Polynome(x):
    '''
    Prend en entrée un argument x et calcule le résultat du polynome x^3-1.5x^2-6x+5

    Paramètre:
            x : un nombre

    Sortie:
            le résultat de la fonction f(x)=x^3-1.5x^2-6x+5
    '''
    return  x**3 - 1.5*x**2 - 6*x + 5


# In[2]:


Polynome(5)

