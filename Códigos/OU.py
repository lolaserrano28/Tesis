# -*- coding: utf-8 -*-
"""
Created on Mon May  8 07:09:23 2023

@author: lolas
"""

import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def OU(T,a,b,sigma,X0,N=1000):
    X = [X0]
    Dt = T/1000
    T_ = np.linspace(0, T, N+1)
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + a*(b-X[i-1])*Dt + sigma*np.sqrt(Dt)*Z 
        X.append(Xi)
    return(T_,X)

plt.plot(OU(10,0.75,0.5,0.1,1,1000)[0],OU(10,0.75,0.5,0.1,1,1000)[1], label = "$X_0 = 1$")
plt.plot(OU(10,0.75,0.5,0.1,0,1000)[0],OU(10,0.75,0.5,0.1,0,1000)[1], label = "$X_0 = 0$")
plt.title("Proceso de Vasicek")
plt.legend()
plt.show()
