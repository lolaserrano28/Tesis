# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:08:00 2023

@author: lolas
"""

import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('default')


def MBE(T, N = 1000):
    l = [np.random.normal(0,T/N) for i in range(N)]
    mb = np.insert(np.cumsum(l),0,0)
    return(mb)

T=2
N=1000
T_ = np.linspace(0, T, N+1)
plt.plot(T_ , MBE(T))
plt.title("Movimiento Browniano Estándar")
plt.show()

#%%
def MB(mu,sigma,x,T,N):
    ran = []
    for i in range(n):
        Z = np.random.normal(0,1)
        W = mu*(T/N) + sigma*np.sqrt(T/N)*Z
        ran.append(W)
    suma = np.cumsum(ran)+x
    mb = np.insert(suma,0,x)
    return(mb)

t=10
n = 10000
X = np.linspace(0,t,n+1)
plt.plot(X,MB(0,1,0,t,n))
plt.title("Movimiento Browniano $\mu=0, \sigma = 1$")
plt.show()

#%%

def MBG_milstein(X0, mu, sigma, T=1, N = 1000):
    X = [X0]
    Dt = T/N
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + mu*X[i-1]*Dt + sigma*X[i-1]*np.sqrt(Dt)*Z + (1/2)*sigma*X[i-1]*Dt*(Z**2-1)
        X.append(Xi)
    return(X)


T_ = np.linspace(0, T, N+1)
for mu in [0,0.25,0.5]:
    plt.plot(T_,MBG_milstein(1,mu,0.1),label = "$\mu=$"+str(mu),linewidth = 1)
plt.title("Movimiento Browniano Geométrico: Milstein")
plt.legend()
plt.show()

for sigma in [0.1,0.5,1.2]:
    plt.plot(T_,MBG_milstein(1,0,sigma),label = "$\sigma=$"+str(sigma),linewidth = 1)
plt.title("Movimiento Browniano Geométrico: Milstein")
plt.legend()
plt.show()

#%%

def MBG_Lamperti(T, X0, mu, sigma, N = 1000):
    X = [X0]
    Dt = T/N
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Ln_Xi = math.log(X[i-1]) + (mu-0.5*sigma**2)*Dt + sigma*np.sqrt(Dt)*Z
        X.append(np.exp(Ln_Xi)) 
    return(X)

plt.plot(MBG_Lamperti(1,1,0,0.1,1000)[0] ,MBG_Lamperti(1,1,0,0.1,1000)[1], label = "$\mu=0$")
plt.plot(MBG_Lamperti(1,1,0.25,0.1,1000)[0] ,MBG_Lamperti(1,1,0.25,0.1,1000)[1], label = "$\mu=0.25$")
plt.plot(MBG_Lamperti(1,1,0.5,0.1,1000)[0] ,MBG_Lamperti(1,1,0.5,0.1,1000)[1], label = "$\mu=0.5$")
plt.title("Movimiento Browniano Geométrico: Lamperti")
plt.legend()
plt.show()

plt.plot(MBG_Lamperti(1,1,0,0.1,1000)[0] ,MBG_Lamperti(1,1,0,0.1,1000)[1], label = "$\sigma=0.1$")
plt.plot(MBG_Lamperti(1,1,0,0.5,1000)[0] ,MBG_Lamperti(1,1,0,0.5,1000)[1], label = "$\sigma=0.5$")
plt.plot(MBG_Lamperti(1,1,0,1.2,1000)[0] ,MBG_Lamperti(1,1,0,1.2,1000)[1], label = "$\sigma=1.2$")
plt.title("Movimiento Browniano Geométrico: Lamperti")
plt.legend()
plt.show()
        