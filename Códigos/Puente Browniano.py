# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:41:57 2023

@author: lolas
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def puente_browniano(T,a,b,N=1000):
    X = [a]
    Dt = T/N
    T_ = np.linspace(0, T, N+1)
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + ((b-X[i-1])/(T-T_[i-1]))*Dt + np.sqrt(Dt)*Z 
        X.append(Xi)
    return(X)

T = 1
a = 0
b = 2
N = 1000
T_ = np.linspace(0, T, N+1)
plt.plot(T_,puente_browniano(T,a,b,N))
plt.plot(T_,puente_browniano(T,a,b,N))
plt.plot(T_,puente_browniano(T,a,b,N))
plt.plot(T_,puente_browniano(T,a,b,N))
plt.axhline(y = a,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.axhline(y = b,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.title("Puente Browniano: Ecuación Diferencial")
plt.show()

#%%
def MB(T, N = 1000):
    l = [np.random.normal(0,T/N) for i in range(N)]
    T_ = np.linspace(0, T, N+1)
    mb = np.insert(np.cumsum(l),0,0)
    return(T_,mb)

def puente_browniano2(T,N=1000):
    T_ = MB(T,N)[0]
    mb = MB(T,N)[1]
    PB = mb - (T_/T)*mb[-1]
    return(T_,PB)

plt.plot(puente_browniano2(T,N)[0],puente_browniano2(T,N)[1])
plt.plot(puente_browniano2(T,N)[0],puente_browniano2(T,N)[1])
plt.plot(puente_browniano2(T,N)[0],puente_browniano2(T,N)[1])
plt.axhline(y = 0,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.title("Puente Browniano: Representación Adelantada")