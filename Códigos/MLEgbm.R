library(here)
source(here("Códigos/MBGeometrico.R"))

T = 10
X0 = 1
mu = 0.7
sigma = 0.2
N = 1000
X = MBG_lamperti(mu,sigma,1,T,N)

T_ = seq(0,T,length.out=N+1)

MLE_gbm <- function(T_,X){
  n = length(T_)-1
  T = T_[length(T_)]
  dt = T/n
  Y = log(X[2:(n+1)]/X[1:n])
  s2 = (1/(n*dt))*sum((Y-mean(Y))^2)
  mu = mean(Y)/dt + s2/2
  return(c(mu,sqrt(s2)))
}
