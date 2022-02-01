#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Création des classes pour gérer les exceptions demandées

# Erreur pour la saisie d'une chaîne de caractères
class StringArgument(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

# Erreur pour la saisie d'un nombre complexe
class ComplexArgument(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

# Erreur pour la saisie d'un nombre négatif
class NegativeArgument(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message
    
# Erreur pour la saisie d'un nombre trop grand
class BigArgument(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

# Erreur pour la saisie d'un nombre trop petit
class SmallArgument(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message


def Polynome(x):
    
    '''
    Prend en entrée un argument x et calcule le résultat du polynome x^3-1.5x^2-6x+5
    Si x est une chaîne de caractères ou un nombre complexe ou un nombre négatif ou
    un nombre très grand ou un nombre très petit, un message d'erreur personnalisé s'affiche.

            Paramètre:
                    a : un nombre

            Sortie:
                    le résultat de la fonction f(x)=x^3-1.5x^2-6x+5
    '''
    
    if type(x) == str:
        raise StringArgument("Could not use string as argument")
        
    elif type(x) == complex:
        raise ComplexArgument("Could not use complex number as argument")
        
    elif x < 0:
        raise NegativeArgument("Could not use negative number as argument")
        
    elif x > 1e10:
        raise BigArgument("Could not use big number as argument")
        
    elif x < 1e-10:
        raise SmallArgument("Could not use small number as argument")
        
    else:
        return  x**3 - 1.5*x**2 - 6*x + 5

