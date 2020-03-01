# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:56:23 2020

@author: Abal Abbas
"""
"""Done by Ousmane Dia"""
import numpy as np 
import scipy.stats as sps
import matplotlib.pyplot as plt 
n, p, N = 20, 0.3, int(1e4)
B = np.random.binomial(n, p, N) 
f = sps.binom.pmf(np.arange(n+1), n, p) 
plt.hist(B,bins=n+1,normed=1,range=(5,n+.5),\
    color="blue",label="loi empirique")
plt.stem(np.arange(n+1),f,"r",label="loi theorique")
plt.legend()
