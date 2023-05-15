# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:40:26 2023

@author: lolas
"""


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def cruce(x1,x2,N =1000):
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


def OU(T,X0,alpha,beta,sigma,N=1000):
    X = [X0]
    Dt = T/1000
    T_ = np.linspace(0, T, N+1)
    for i in range(1,N+1):
        Z = np.random.normal(0,1)
        Xi = X[i-1] + alpha*(beta-X[i-1])*Dt + sigma*np.sqrt(Dt)*Z 
        X.append(Xi)
    return(T_,X)

def puente_OU(T,a,b,alpha,beta,sigma,N=1000):
    c = False
    while c==False:
        X1 = OU(T,a,alpha, beta, sigma,N)
        X2 = OU(T,b,alpha, beta, sigma,N)
        x1 = X1[1]
        x2 = np.flip(X2[1])
        if cruce(x1,x2,N=1000) == False:
            c = False
        else:
            nu = cruce(x1,x2,N=1000)[1]
            y1 = x1[0:nu]
            y2 = x2[nu:1001]
            X = np.concatenate((y1,y2))
            c = True
    return(X1[0],X,nu)
            

    
a = 5
b = 8
T = 10
alpha = 0.1
beta = 6
sigma = 0.5
N = 1000

"""
X1 = OU(T,a,alpha, beta, sigma,N)
X2 = OU(T,b,alpha, beta, sigma,N)
print(cruce(X1,X2,N))

plt.plot(X1[0],X1[1],label = "X1")
plt.plot(X2[0],np.flip(X2[1]),label = "X2")
"""
plt.axhline(y = a,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.axhline(y = b,xmin = 0, xmax = T, linestyle = "--", color = "#458f75")
plt.plot(puente_OU(T,a,b,alpha,beta,sigma,N)[0],puente_OU(T,a,b,alpha,beta,sigma,N)[1])
plt.plot(puente_OU(T,a,b,alpha,beta,sigma,N)[0],puente_OU(T,a,b,alpha,beta,sigma,N)[1])
plt.plot(puente_OU(T,a,b,alpha,beta,sigma,N)[0],puente_OU(T,a,b,alpha,beta,sigma,N)[1])
plt.title("Puente Vasicek")

plt.show()

        
    
        


