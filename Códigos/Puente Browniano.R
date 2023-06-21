#Función que simula un (0,a,T,b)-puente browniano
puente_browniano <- function(a,b,T,N){
  dt = T/N
  X = numeric(N+1)
  X[1] = a
  T_ = seq(0,T,length.out=N+1)
  for(i in 1:N){
    Z = rnorm(1,0,1)
    X[i+1] = X[i] + ((b-X[i])/(T-T_[i]))*dt + sqrt(dt)*Z
  }
  return(X)
}

T=1
N=1000
T_ = seq(0,T,length.out=N+1)
plot(T_,puente_browniano(1,2,T,N), main = "Puente Browniano",
    xlab = "t",ylab = "Xt",type = "l")
lines(T_, puente_browniano(1,2,T,N))

  