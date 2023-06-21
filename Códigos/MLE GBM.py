# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:43:39 2023

@author: lolas
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import math

def MBG_Lamperti(T, X0, mu, sigma, N = 1000):
    X = [X0]
    Dt = T/N
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Ln_Xi = math.log(X[i-1]) + (mu-0.5*sigma**2)*Dt + sigma*np.sqrt(Dt)*Z
        X.append(np.exp(Ln_Xi)) 
    return(X)




def MLE(X,T_):
    n = len(T_)-1
    T = T_[-1]
    dt = T/n
    Y = np.log(np.divide(X[1:n],X[0:n-1]))
    s2 = sum((Y-np.mean(Y))**2)*(1/(n*dt))
    mu = np.mean(Y)/dt+s2/2
    sigma = np.sqrt(s2)
    return(mu,sigma)


T = 10
X0 = 1
N = 1000
mu_real = 0.5
sigma_real = 0.2
X = MBG_Lamperti(T,X0,mu_real,sigma_real,N)

T_ = np.linspace(0, T, N+1)
mu_ = []
s_ = []
for i in range(2,N+1):
    x = X[0:i]
    t = T_[0:i]
    mu = MLE(x,t)[0]
    sigma = MLE(x,t)[1]
    mu_.append(mu) 
    s_.append(sigma)
    
plt.axhline(y = mu_real,xmin = 0, xmax = T, linestyle = "--", c = "r")
plt.scatter([*range(0,N-1,1)],mu_,marker = ".",facecolors='none', edgecolors='#1f77b4')
plt.ylabel("Estimador $\mu$")
plt.xlabel("Número de Observaciones")
plt.show()


plt.axhline(y = sigma_real,xmin = 0, xmax = T, linestyle = "--",c = "r")
plt.scatter([*range(0,N-1,1)],s_,facecolors='none', edgecolors='#2ca02c',marker = ".")
plt.ylabel("Estimador $\sigma$")
plt.xlabel("Número de observaciones")
plt.show()

