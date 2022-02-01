#!/usr/bin/env python
# coding: utf-8

# In[1]:


# b) Fonction factorielle

def factorielle(n: int):
    '''
    Prend en entrée un argument n et calcule la factorielle de n

    Paramètre:
            n : un entier naturel

    Sortie:
            res : la factorielle de n
    '''
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(2, n+1):
            res = res * i
    return res


# In[2]:


factorielle(5)

