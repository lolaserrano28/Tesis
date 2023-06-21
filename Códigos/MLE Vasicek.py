# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:40:30 2023

@author: lolas
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def OU(T,X0,a,b,sigma,N=1000):
    X = [X0]
    Dt = T/1000
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + a*(b-X[i-1])*Dt + sigma*np.sqrt(Dt)*Z 
        X.append(Xi)
    return(X)

T = 10
N = 1000
X0_1 = 0
a_real = 1
b_real = 3
sigma_real = 2
T_ = np.linspace(0, T, N+1)
X = OU(T,X0_1,a_real,b_real,sigma_real,N)

#La función recibe como parámetros una partición del intervalo temporal [0,T]
#y la muestra de observaciones para cada tiempo de la partición
def MLE_a(T_, X):
    n = len(T_)-1
    dt = T_[1]-T_[0]
    suma1 = n*sum([X[i+1]*X[i] for i in range(n)])
    suma2 = sum([X[i+1] for i in range(n)])*sum([X[i] for i in range(n)])
    suma3 = n*sum([X[i]**2 for i in range(n)])
    suma4 = sum([X[i] for i in range(n)])**2
    a = (-1/dt)*np.log((suma1-suma2)/(suma3-suma4))  
    return(a)

def MLE_b(T_, X, a):
    n = len(T_)-1
    dt = T_[1]-T_[0]
    expo = np.exp(-a*dt)
    suma1 = sum([X[i+1] for i in range(n)])
    suma2 = sum([X[i] for i in range(n)])
    b = (1/(n*(1-expo)))*(suma1-expo*suma2)
    return(b)

def MLE_sigma(T_, X, a, b):
    n = len(T_)-1
    dt = T_[1]-T_[0]
    expo = np.exp(-a*dt)
    expo2 = np.exp(-2*a*dt)
    suma = sum([(X[i+1]- X[i]*expo - b*(1-expo))**2 for i in range(n)])
    sigma = np.sqrt((2*a)/(n*(1-expo2))*suma)
    return(sigma)

def MLE_vasicek(T_,X):
    a = MLE_a(T_,X)
    b = MLE_b(T_, X, a)
    sigma = MLE_sigma(T_, X, a, b)
    return(np.array([a,b,sigma]))

parametros = MLE_vasicek(T_,X)
print(parametros)

#%%
def beta_1(X):
    n = len(X)-1
    suma1 = sum([X[i+1]*X[i] for i in range(n)])
    suma2 = sum([X[i+1] for i in range(n)])
    suma3 = sum([X[i] for i in range(n)])
    suma4 = sum([X[i]**2 for i in range(n)])
    b1 = ((n**(-1))*suma1 - (n**(-2))*suma2*suma3) / ( (n**(-1))*suma4-(n**(-2))*(suma3**2) )
    return(b1)

def beta_2(X,b1):
    n = len(X)-1
    suma = sum([X[i+1]-b1*X[i] for i in range(n)])
    b2 = (n**(-1))*suma/(1-b1)
    return(b2)

def beta_3(X,b1,b2):
    n = len(X)-1
    b3 = (1/n)*sum([(X[i+1]-b1*X[i]-b2*(1-b1))**2 for i in range(n)])
    return(b3)

def MLE2(X):
    dt = (len(X)-1)**(-1)
    b1 = beta_1(X)
    b2 = beta_2(X,b1)
    b3 = beta_3(X,b1,b2)
    a = -(1/dt)*np.log(b1)
    b = b2
    sigma = 2*a*b3*(1-b1**2)**(-1)
    return(a,b,sigma)
#%% PRUEBA CONSISTENCIA

a_ = []
b_ = []
s_ = []
for i in range(2,N+1):
    x = X[0:i]
    t = T_[0:i]
    a = MLE_vasicek(t,x)[0]
    b = MLE_vasicek(t,x)[1]
    sigma = MLE_vasicek(t,x)[2]
    a_.append(a) 
    b_.append(b)
    s_.append(sigma)
    
plt.axhline(y = a_real,xmin = 0, xmax = T, linestyle = "--", c = "r")
plt.scatter([*range(0,N-1,1)],a_,marker = ".",facecolors='none', edgecolors='#1f77b4')
plt.xlabel("Número de observaciones")
plt.ylabel("Estimador $a$")
plt.show()

plt.axhline(y = b_real,xmin = 0, xmax = T, linestyle = "--",c = "r")
plt.scatter([*range(0,N-1,1)],b_, facecolors='none', edgecolors='#9467bd',marker = ".")
plt.xlabel("Número de observaciones")
plt.ylabel("Estimador $b$")
plt.show()

plt.axhline(y = sigma_real,xmin = 0, xmax = T, linestyle = "--",c = "r")
plt.scatter([*range(0,N-1,1)],s_,facecolors='none', edgecolors='#2ca02c',marker = ".")
plt.xlabel("Número de observaciones")
plt.ylabel("Estimador $\sigma$")
plt.show()

#%%
#Prueba de Kolmogorov Smirnov
n = 200
muestra = []
for i in range(n):
    X=OU(T,X0_1,a_real,b_real,sigma_real,N) 
    vec = (MLE_vasicek(T_, X)-np.array([a_real,b_real, sigma_real]))*N
    muestra.append(vec)
    
    


