#Funciones para movimiento browniano estándar y movimiento browniano con deriva y difusion

MBE <- function(T,N){
  l <- c(0,rnorm(N,0,T/N))
  mb <- cumsum(l)
  return(mb)
}

T = 1
N = 1000
T_ = seq(0,T,length.out=N+1)
plot(T_,MBE(T,N),type="l",main = "Movimiento Browniano",xlab = "T",ylab = "Mov. Browniano")


MB <- function(mu,sigma,x,T,N){
  l <- c(x,rnorm(N,mu*(T/N),sigma^2*(T/N)))
  mb <- cumsum(l)
  return(mb)
}

plot(T_,MB(1,1.5,0,T,N),type="l",main = "Movimiento Browniano: mu = 1, sigma = 1.5",xlab = "T",ylab = "Mov. Browniano")


