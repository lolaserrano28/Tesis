# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:08:00 2023

@author: lolas
"""

import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def MB(T, N = 1000):
    l = [np.random.normal(0,T/N) for i in range(N)]
    T_ = np.linspace(0, T, N+1)
    mb = np.insert(np.cumsum(l),0,0)
    return(T_,mb)

plt.plot(MB(2)[0] ,MB(2)[1])
plt.title("Movimiento Browniano Estándar")
plt.show()

#%%

def MBG_milstein(T, X0, mu, sigma, N = 1000):
    X = [X0]
    Dt = T/1000
    T_ = np.linspace(0, T, N+1)
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + mu*X[i-1]*Dt + sigma*X[i-1]*np.sqrt(Dt)*Z + (1/2)*sigma*X[i-1]*Dt*(Z**2-1)
        X.append(Xi)
    return(T_,X)

plt.plot(MBG_milstein(1,1,0,0.1,1000)[0] ,MBG_milstein(1,1,0,0.1,1000)[1], label = "$\mu=0$")
plt.plot(MBG_milstein(1,1,0.25,0.1,1000)[0] ,MBG_milstein(1,1,0.25,0.1,1000)[1], label = "$\mu=0.25$")
plt.plot(MBG_milstein(1,1,0.5,0.1,1000)[0] ,MBG_milstein(1,1,0.5,0.1,1000)[1], label = "$\mu=0.5$")
plt.title("Movimiento Browniano Geométrico: Milstein")
plt.legend()
plt.show()

plt.plot(MBG_milstein(1,1,0,0.1,1000)[0] ,MBG_milstein(1,1,0,0.1,1000)[1], label = "$\sigma=0.1$")
plt.plot(MBG_milstein(1,1,0,0.5,1000)[0] ,MBG_milstein(1,1,0,0.5,1000)[1], label = "$\sigma=0.5$")
plt.plot(MBG_milstein(1,1,0,1.2,1000)[0] ,MBG_milstein(1,1,0,1.2,1000)[1], label = "$\sigma=1.2$")
plt.title("Movimiento Browniano Geométrico: Milstein")
plt.legend()
plt.show()

#%%

def MBG_Lamperti(T, X0, mu, sigma, N = 1000):
    X = [X0]
    Dt = T/1000
    T_ = np.linspace(0, T, N+1)
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Ln_Xi = math.log(X[i-1]) + (mu-0.5*sigma**2)*Dt + sigma*np.sqrt(Dt)*Z
        X.append(np.exp(Ln_Xi)) 
    return(T_,X)

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
        