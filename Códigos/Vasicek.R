#Función que simula un proceso de Vasicek/Orstein-Uhlenbeck
vasicek <- function(a,b,sigma,X0,T,N){
  dt = T/N
  X <- numeric(N+1)
  X[1] = X0
  for(i in 1:N){
    Z = rnorm(1,0,1)
    X[i+1] = X[i] + a*(b-X[i])*dt + sigma*sqrt(dt)*Z 
  }
  return(X)
}

#T = 1
#N = 1000
#T_ = seq(0,T,length.out=N+1)

#plot(T_,vasicek(0.1,0.5,0.2,1,T,N), main = "Proceso de Vasicek",
 #    xlab = "t",ylab = "Xt",type = "l")
