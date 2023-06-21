library(here)
source(here("Códigos/Vasicek.R"))
source(here("Códigos/MBGeometrico.R"))

a = 0.1
b = 0.5
sigma = 0.2

alpha = 1
beta = 2

T = 1
N = 100


#La función cruce(x1,x2) indica si hay un cruce en las trayectorias y la posición

#En esta funcion x1[1] = alpha y x2[N] = beta 
#(ie la trayectoria x2 ya está a tiempo reverso)
cruce <- function(x1,x2){
  v <- c(x1>x2)
  #Caso donde no hay cruce
  if(sum(v)==0|sum(v)==length(v)){
    bool = FALSE
    nu = 0
  }else{
    #Caso donde x1[1]>x2[1]
    if(v[1]==TRUE){
      nu = which(v==FALSE)[1]
    #Caso donde x1[1]<x2[1]
    }else{
      nu = which(v==TRUE)[1]
    }
    bool = TRUE
  }
  return(c(bool,nu))
}

T_ = seq(0,T,length.out=N+1)
x1 <- vasicek(a,b,sigma,alpha,T,N)
x2 <- vasicek(a,b,sigma,beta,T,N)
x2 <- rev(x2)
v<-c(x1>x2)
v

plot(T_,x1,type="l",col=1)
lines(T_,x2,type="l",col=2)

cruce(x1,x2)

#borrador de la funcion con pruebas
puente_vasicek_pruebas <- function(alpha,beta,a,b,sigma,T,N){
  bool = FALSE
  while(bool == FALSE){
    x1 <- vasicek(a,b,sigma,alpha,T,N)
    x2 <- rev(vasicek(a,b,sigma,beta,T,N))
    if(cruce(x1,x2)[1]==0){
      bool = FALSE
    }else{
      nu = cruce(x1,x2)[2]
      y1 = x1[0:(nu-1)]
      y2 = x2[nu:(N+1)]
      X = c(y1,y2)
      bool = TRUE
    }
  }
  return(list(X,x1,x2))
}
prueba=puente_vasicek_pruebas(alpha,beta,a,b,sigma,T,N)
plot(T_,prueba[[1]],type="l",col=1,lwd=2)
lines(T_,prueba[[2]],type="l",col=2,lty=2)
lines(T_,prueba[[3]],type="l",col=3,lty=3)

#Función bien: devuelve solo el puente de vasicek
puente_difusion <- function(fun,alpha,beta,T,N,theta1,theta2,theta3=NULL){
  bool = FALSE
  while(bool == FALSE){
    #1=vasicek, 2=MBG
    if(fun == 1){
      x1 <- vasicek(theta1,theta2,theta3,alpha,T,N)
      x2 <- rev(vasicek(theta1,theta2,theta3,beta,T,N))
    }else if(fun==2){
      x1 <- MBG(theta1,theta2,alpha,T,N)
      x2 <- rev(MBG(theta1,theta2,beta,T,N))
    }
    if(cruce(x1,x2)[1]==0){
      bool = FALSE
    }else{
      nu = cruce(x1,x2)[2]
      y1 = x1[0:(nu-1)]
      y2 = x2[nu:(N+1)]
      X = c(y1,y2)
      bool = TRUE
    }
  }
  return(X)
}

mu = 0.25
s = 0.1
alpha = 1
beta = 2


#Pruebas para puente OU
plot(T_,puente_difusion(1,alpha,beta,T,N,a,b,sigma),type = "l",col = "#FF6699",
     ylab="X",xlab="T",main="Puentes de Vasicek")
lines(T_,puente_difusion(1,alpha,beta,T,N,a,b,sigma),type = "l",col = "#660099")
lines(T_,puente_difusion(1,alpha,beta,T,N,a,b,sigma),type = "l",col = "#00CC88")
lines(T_,puente_difusion(1,alpha,beta,T,N,a,b,sigma),type = "l",col = "#FF9933")
abline(h=alpha, lwd = 2,lty=2)
abline(h=beta,lwd=2,lty=2)



mu = 0.3
s = 1
alpha = 1
beta = 1
#Pruebas puente MBG
plot(T_,puente_difusion(2,alpha,beta,T,N,mu,sigma),type = "l",col = "#FF6699",
     ylab="X",xlab="T",main="Puentes Mov. Browniano Geométrico",ylim = c(0,2))
lines(T_,puente_difusion(2,alpha,beta,T,N,mu,sigma),type = "l",col = "#660099")
lines(T_,puente_difusion(2,alpha,beta,T,N,mu,sigma),type = "l",col = "#00CC88")
lines(T_,puente_difusion(2,alpha,beta,T,N,mu,sigma),type = "l",col = "#FF9933")
abline(h=alpha, lwd = 2,lty=2)
abline(h=beta,lwd=2,lty=2)
