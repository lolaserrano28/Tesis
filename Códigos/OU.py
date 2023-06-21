# -*- coding: utf-8 -*-
"""
Created on Mon May  8 07:09:23 2023

@author: lolas
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

def OU(T,X0,a,b,sigma,N=1000):
    X = [X0]
    Dt = T/N
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + a*(b-X[i-1])*Dt + sigma*np.sqrt(Dt)*Z 
        X.append(Xi)
    return(X)

"""
T = 10
N = 1000
sigma = 0.1
X0_1 = 1
X0_2 = 0
a1 = 0.1
a2 = 1
sigma = 0.2
b = (X0_1+X0_2)/2
T_ = np.linspace(0, T, N+1)


plt.plot(T_,OU(T,X0_1,a1,b,sigma,N), label = "$X_0 = 1, a = 0.1$")
plt.plot(T_,OU(T,X0_2,a2,b,sigma,N), label = "$X_0 = 0, a = 1$")
plt.title("Proceso de Vasicek")
plt.legend()
plt.show()


plt.plot(T_,OU(10,1,1, 2, 0.1,1000), label = "$b = 2 , \sigma = 0.1$")
plt.plot(T_,OU(10,1,1,0.5,0.3,1000), label = "$b = 0.5, \sigma = 0.3$")
plt.title("Proceso de Vasicek")
plt.legend()
plt.show()
"""

