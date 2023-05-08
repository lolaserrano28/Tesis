#____________________________________________________________________________ 
#                                                                           
#                          Ejemplo Monte Carlo               
#____________________________________________________________________________


#Esperanza y sd
N = 1000000
X <- rnorm(N)
Y <- exp(b*X)

esp <- exp(b^2/2)
sd <- sqrt(exp(2*b^2)-exp(b^2))

mc.Esp <- mean(Y)
mc.Esp

mc.sd <- sd(y)
mc.sd


#Intervalos de confianza
I1 <- mc.Esp - sd*1.96/sqrt(N)
I2 <- mc.Esp + sd*1.96/sqrt(N)

i1 <- mc.Esp - mc.sd*1.96/sqrt(N)
i2 <- mc.Esp + mc.sd*1.96/sqrt(N)


plot(1:N,cumsum(Y)/(1:N), type ="l" , axes =F , xlab =" n", ylim =c(0,350000))
axis(1 , seq (0 ,N , length =5))
axis(2 , seq (0 ,350000 , length =6))
abline(h =268337.3) # true value
abline(h= i1 , lty =3) # MC conf interval
abline(h= i2, lty =3)
abline(h= mc.Esp , lty =2) # MC estimate
box()
