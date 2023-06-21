# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:38:06 2023

@author: lolas
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from PuenteDifusion import cruce, puente_OU
from OU import OU



#%% Implementación algoritmo puente de Vasicek2

T = 1
N = 100
theta = 0.5
sigma = 1
X0 = 0

def Xi(X0,theta, sigma,T,N):
    X = [X0]
    dt = T/N
    var = (sigma**2)*(1-np.exp(-2*theta*dt))/(2*theta)
    for i in range(1,N+1):
        wi = np.random.normal(0, np.sqrt(var))
        xi = np.exp(-theta*dt)*X[i-1] + wi
        X.append(xi)
    return(X)

p=Xi(X0,theta,sigma,T,N)

def Zi(X0,x,theta,sigma,T,N):
    X = Xi(X0,theta,sigma,T,N)
    T_ = np.linspace(0,T,N+1)
    Z = [X[0]]
    for i in range(1,N+1):
        zi = X[i]+(x-X[-1])*(np.exp(theta*T_[i])-np.exp(-theta*T_[i]))/(np.exp(theta*T_[-1])-np.exp(-theta*T_[-1]))
        Z.append(zi)
    return(Z)

T_ = np.linspace(0,T,N+1)
x=0
#Z = Zi(X0,x,theta,sigma,T,N)
#plt.plot(T_, Z)
#plt.show()

#%% Muchas simulaciones de este puente. Nos fijamos en el tiempo t = 0.5

"""
sim1 = []
sim2 = []
for i in range(25000):
    X1 = puente_OU(T,X0,x,theta,0,sigma,N)
    X2 = Zi(X0,x,theta,sigma,T,N)
    sim1.append(X1[500])
    sim2.append(X2[500])
    
    
#%%QQPLOT
plt.scatter(np.sort(sim1), np.sort(sim2))
plt.xlabel('Puente Aproximado')
plt.ylabel("Puente Exacto")
plt.show()
"""

        



    