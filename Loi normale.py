# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:36:02 2020

@author: Abal Abbas
"""
"""Done By Ousmane Dia"""
import numpy as np
import matplotlib.pyplot as plt

mu = 10.0
sigma = 2.0

data = np.random.randn(100000) * sigma + mu

hx, hy, _ = plt.hist(data, bins=50, normed=1,color="lightblue")

plt.ylim(0.0,max(hx)+0.05)
plt.title('Generer des valeurs aléatoires depuis ddepuis une loi normale avec python')
plt.grid()

plt.savefig("numpy_random_numbers_normal_distribution.png", bbox_inches='tight')
plt.show()
