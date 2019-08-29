
# coding: utf-8

# In[ ]:

def call_americano_arbol(S0,T,r,sigma,K,N): #precio inicial, tiempo, tasa, volatilidad, strike, n° de pasos

    import random 
    import numpy as np
    import scipy.optimize as optimization

    delta_t=T/N
    u=np.exp(sigma*np.sqrt(delta_t))
    d=1/u
    p=(np.exp(r*delta_t)-d)/(u-d)

    S = [[S0*u**(j-i)*d**i for i in range(j+1)] for j in range(N+1)] #construcción de los precios del activo
    P = [[0 for i in range(j+1)] for j in range(N+1)] #precio del call

    def max(a,b): #máximo
        z=a
        if a<b:
            z=b
        return z    
	
    for i in range(N+1): #valor del derivado a tiempo T
        P[N][i]=max(S[N][i]-K,0)
    
    for j in range(N):
        for i in range(N-j):
            P[N-1-j][i]=max(np.exp(-r*delta_t)*(p*P[N-j][i]+(1-p)*P[N-j][i+1]),S[N-1-j][i]-K) #completar en forma backward el arbol
    return P[0][0]

def main():
    asset_price = 0.0893387669853
    maturity_time = 1/(12*366)
    interest_rate = 1
    volatility = 0.275799155
    interval = 36

    print(call_americano_arbol(asset_price, maturity_time, interest_rate, volatility, asset_price, interval))

if __name__ == "__main__":
	main()