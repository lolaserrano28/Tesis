# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:40:26 2023

@author: lolas
"""


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')


def cruce(x1,x2,N):
    if (a >= b):
        l = [i for i in range(N+1) if x1[i] <= x2[i]]
        if l==[]:
            return(False)
        else:
            nu = l[0]
            return (True, nu)
    elif (a < b):
        l = [i for i in range(N+1) if x1[i] >= x2[i]]
        if l==[]:
            return(False)
        else:
            nu = l[0]
            return (True, nu)


def OU(T,X0,alpha,beta,sigma,N):
    X = [X0]
    Dt = T/N
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + alpha*(beta-X[i-1])*Dt + sigma*np.sqrt(Dt)*Z 
        X.append(Xi)

    return(X)

def puente_OU(T,a,b,alpha,beta,sigma,N):
    c = False
    while c==False:
        x1 = OU(T,a,alpha, beta, sigma,N)
        x2 = np.flip(OU(T,b,alpha, beta, sigma,N))
        if cruce(x1,x2,N) == False:
            c = False
        else:
            nu = cruce(x1,x2,N)[1]
            y1 = x1[0:nu]
            y2 = x2[nu:N+1]
            X = np.concatenate((y1,y2))
            c = True
    return(X)
            

#%%  
  
a = 5
b = 8
T = 1
alpha = 0.1
beta = 6
sigma = 0.5
N = 100
T_ = np.linspace(0, T, N+1)

plt.axhline(y = a,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.axhline(y = b,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.plot(T_,puente_OU(T,a,b,alpha,beta,sigma,N))
plt.plot(T_,puente_OU(T,a,b,alpha,beta,sigma,N))
plt.plot(T_,puente_OU(T,a,b,alpha,beta,sigma,N))
plt.title("Puente Vasicek")

plt.show()

#%%
a = 0
b = 0
T = 1
alpha = 0.5
beta = 0
sigma = 1
N = 100
T_ = np.linspace(0, T, N+1)



plt.axhline(y = a,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.axhline(y = b,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.plot(T_,puente_OU(T,a,b,alpha,beta,sigma,N))
plt.plot(T_,puente_OU(T,a,b,alpha,beta,sigma,N))
plt.plot(T_,puente_OU(T,a,b,alpha,beta,sigma,N))
plt.title("Puente Vasicek")

plt.show()
        
    
        


