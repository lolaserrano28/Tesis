library(here)
install.packages("MVN")
library("MVN")
source(here("Códigos/Vasicek.R"))
source(here("Códigos/MLEVasicek.R"))


#Consistencia del estimador
T = 10
N = 1000
X0 = 0
a_real = 1
b_real = 3
sigma_real = 2
T_ = seq(0,T,length.out=N+1)
X = vasicek(a_real,b_real,sigma_real,X0,T,N)

a_ = numeric(N)
b_ = numeric(N)
s_ = numeric(N)
for(i in 3:(N+1)){
  x = X[1:i]
  t = T_[1:i]
  a_[i] = MLE_vasicek(t,x)[1]
  b_[i] = MLE_vasicek(t,x)[2]
  s_[i] = MLE_vasicek(t,x)[3]
}

plot(a_,main="Consistencia Estimador a",pch=1,cex = 0.5)
abline(h=a_real)

plot(T_,b_,main="Consistencia Estimador b",pch=1,cex = 0.5)
abline(h=b_real)

plot(T_,s_,main="Consistencia Estimador sigma",pch=1,cex = 0.5)
abline(h=sigma_real)

#Matriz de Fisher
fisher_vasicek <- function(T_,X){
  theta = MLE_vasicek(T_,X)
  n = length(T_)-1
  T = T_[length(T_)]
  dt = T/n
  a = theta[1]
  b = theta[2]
  s = theta[3]
  ex2 = exp(-2*a*dt)
  f11 = -((2*a*dt^2*ex2*sum((X[1:n]-b)^2))/(s^2*(1-ex2))) - (n*ex2^2*(ex2^(-1)-2*a*dt-1)^2)/(2*a*(1-ex2)^2)
  f12 = (2*a*dt*sum(X[1:n]-b))/(s^2*(1+ex2^(-0.5)))
  f13 = (n*(1-ex2*(2*a*dt+1)))/(s*a*(1-ex2))
  f22 = -(2*n*a*(1-ex2^(0.5)))/(s^2*(1+ex2^(0.5)))
  f33 = -(2*n)/s^2
  matriz <- matrix( c(f11,f12,f13,
                      f12,f22,0,
                      f13,0,f33),nrow = 3,byrow = TRUE)
  return(matriz)
}

fisher_vasicek(T_,X)

#Normalidad Asintótica
T = 10
N = 1000
X0 = 0
a_real = 1
b_real = 3
sigma_real = 2
T_ = seq(0,T,length.out=N+1)
n = 100
muestra_estimadores = matrix(NA,n,3)
for(i in 1:n){
  X = vasicek(a_real,b_real,sigma_real,X0,T,N) 
  muestra_estimadores[i,] = (MLE_vasicek(T_, X)-c(a_real,b_real, sigma_real))*N
}
mvn(data = muestra_estimadores,mvnTest = "mardia")$multivariateNormality



