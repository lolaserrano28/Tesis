



#Consistencia del estimador
T = 10
N = 1000
X0 = 1
mu_real = 0.5
sigma_real = 0.2
T_ = seq(0,T,length.out=N+1)
X = MBG_milstein(mu_real,sigma_real,X0,T,N)

mu_ = numeric(N)
s_ = numeric(N)
for(i in 3:(N+1)){
  x = X[1:i]
  t = T_[1:i]
  mu_[i] = MLE_gbm(t,x)[1]
  s_[i] = MLE_gbm(t,x)[2]
}

plot(mu_,main="Consistencia Estimador mu",pch=1,cex = 0.5)
abline(h=mu_real)

plot(T_,s_,main="Consistencia Estimador sigma",pch=1,cex = 0.5)
abline(h=sigma_real)


#Normalidad Asintótica
n = 100
muestra_estimadores = matrix(NA,n,2)
for(i in 1:n){
  X = MBG(mu_real,sigma_real,X0,T,N) 
  muestra_estimadores[i,] = (MLE_gbm(T_,X)-c(mu_real,sigma_real))*N
}
mvn(data = muestra_estimadores,mvnTest = "mardia")$multivariateNormality
