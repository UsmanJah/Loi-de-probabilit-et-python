# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:28:46 2020

@author: Abal Abbas
"""
"""Done by Ousmane Dia"""
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt 
E = np.random.randn(int(1e5))#echantillon 
x = np.linspace(4,4,1000)
f_x = sps.norm.pdf(x) #Densite gaussienne 
plt.plot(x,f_x,"r",label="Theorie") 
#Affichage histo: 
plt.hist(E,bins=50,normed=1,label="Données")
plt.legend(loc="best")
