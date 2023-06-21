#Funciones para movimiento browniano geométrico: usando Milstein y Lamperti

MBG_milstein <- function(mu,sigma,X0,T,N){
  dt = T/N
  X <- numeric(N+1)
  X[1] = X0
  for(i in 1:N){
    Z = rnorm(1,0,1)
    X[i+1] = X[i] + mu*X[i]*dt + sigma*X[i]*sqrt(dt)*Z + 0.5*sigma*X[i]*dt*(Z^2-1)
  }
  return(X)
}

T = 1
N = 1000
T_ = seq(0,T,length.out=N+1)

#X = MBG_milstein(0,0.1,1,T,N)

#plot(T_,X, type = "l", 
#     main = "Movimiento Browniano Geométrico: Milstein", 
#     sub = "mu = 0, sigma = 0.1",
#     xlab = "T", ylab = "M.B. Geométrico")  


#Movimiento browniano geométrico usando Lamperti
MBG <- function(mu,sigma,X0,T,N){
  dt = T/N
  X <- numeric(N+1)
  X[1] = X0
  for(i in 1:N){
    Z = rnorm(1,0,1)
    ln_xi = log(X[i]) + (mu-0.5*sigma^2)*dt + sigma*sqrt(dt)*Z
    X[i+1] = exp(ln_xi)
  }
  return(X)
}

#X = MBG_lamperti(0,0.1,1,T,N)

#plot(T_,X, type = "l", 
 #    main = "Movimiento Browniano Geométrico: Lamperti", 
 #    sub = "mu = 0, sigma = 0.1",
 #    xlab = "T", ylab = "M.B. Geométrico") 
