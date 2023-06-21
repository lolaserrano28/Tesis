library(here)
source(here("Códigos/Puente Difusion.R"))

#Usando el Lemma 3.1 de Bridges se calibra el puente de Vasicek con el puente exacto
Xi <- function(theta,sigma,x0,T,N){
  dt = T/N
  X <- numeric(N+1)
  X[1] = x0
  var = (sigma^2)*(1-exp(-2*theta*dt))/(2*theta)
  for (i in 1:N){
    W <- rnorm(1,0,sqrt(var))
    X[i+1] <- X[i]*exp(-theta*dt) + W 
  }
  return(X)
}

Zi <- function(theta,sigma,x0,x,T,N){
  X <- Xi(theta, sigma, x0, T, N)
  Z <- numeric(N+1)
  Z[1] <- x0
  xN <- tail(X,1)
  T_ = seq(0,T,length.out=N+1)
  for (i in 1:(N+1)){
    Z[i] <- X[i] + (x-xN)*(exp(theta*T_[i])-exp(-theta*T_[i]))/(exp(theta*tail(T_,1))-exp(-theta*tail(T_,1)))
  }
  return(Z)
}

T = 1
N = 100
theta = 0.5
sigma = 1
x = 0
x0 = 0


M = 25000
sim_aproximado <- numeric(M)
sim_exacto <- numeric(M)
for (i in 1:M){
  sim_aproximado[i] <- puente_vasicek(x0,x,theta,0,sigma,T,N)[N/2+1]
  sim_exacto[i] <- Zi(theta,sigma,x0,x,T,N)[N/2+1]
}

T_ = seq(0,T,length.out=N+1)

plot(T_,puente_vasicek(x0,x,theta,0,sigma,T,N),type = "l",col = "#FF6699",
     ylab="Xt",xlab="T",main="Puentes de Vasicek: Aproximación",lwd=1.5,ylim=c(-1,1))
lines(T_,puente_vasicek(x0,x,theta,0,sigma,T,N),type = "l",col = "#660099",lwd=1.5)
lines(T_,puente_vasicek(x0,x,theta,0,sigma,T,N),type = "l",col = "#00CC88",lwd=1.5)
lines(T_,puente_vasicek(x0,x,theta,0,sigma,T,N),type = "l",col = "#FF9933",lwd=1.5)
abline(h=0, lwd = 2,lty=2)

plot(T_,Zi(theta,sigma,x0,x,T,N),type = "l",col = "#FF6699",
     ylab="Xt",xlab="T",main="Puentes de Vasicek: Exacto",lwd=1.5,ylim=c(-1,1))
lines(T_,Zi(theta,sigma,x0,x,T,N),type = "l",col = "#660099",lwd=1.5)
lines(T_,Zi(theta,sigma,x0,x,T,N),type = "l",col = "#00CC88",lwd=1.5)
lines(T_,Zi(theta,sigma,x0,x,T,N),type = "l",col = "#FF9933",lwd=1.5)
abline(h=0, lwd = 2,lty=2)


qqplot(sim_exacto, sim_aproximado, 
       main="Gráfico Q-Q puente Vasicek",
       xlab="Puente Exacto",
       ylab="Puente Aproximado")
abline(0,1, lwd = 2,col="blue")

