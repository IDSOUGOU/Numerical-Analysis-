# Resolution of Differential Equation n°2 by using the 'RK4' method
import matplotlib.pyplot as plt
import numpy as np


def rk4 ( f ,X0 , t ):                                 # Runge Kutta -  order 4
# Inputs   : t : Contains the points of the subdivision //  X0 : the initial conditions
# Outputs  : X : Approaches to t-points
    n = len (t )
    X = np . zeros ((n,) + np.shape(X0))               # "zeros" returns a matrix of 0 // "shape" returns the size of the array
    X [0]= X0                                          # store initial values
    for i in range (n -1):
        k1 = f ( X[ i ] ,t [ i ])                      # k1 = f(y , t)
        h = (t [i +1] - t [ i ])/2
        k2 = f (X [ i ]+ h * k1 , t [i ]+ h)
        k3 = f (X [ i ]+ h * k2 , t [i ]+ h)
        k4 = f (X [ i ]+2* h* k3 ,t [ i ]+2* h )
        X [i +1]= X [i ]+ h /3*( k1 +2* k2 +2* k3 + k4 )# we have already divided h by 2
    return X
    
def g (Y , t ):
        y,dy = Y                                        # we take g = 9.8 m/s and a = 3 m
        return ( np.array([dy,-(3/4)*(9.8/3)*np.cos( y) ] ))
 
t = np . linspace (0 ,20 ,1000)                         # cutting the interval [20, 0] to 1000
ci = np . array ([0 ,0])                                # initial conditions (y(0) , y′(0)) = (0 , 0)
sol2 = rk4 (g , ci , t )                                # solution by using RK4

# Variation of theta over time 
plt.figure (3)
plt.title ( " Curious Oscillator n°2 -- RK4 -- " )
plt.plot (t , sol2 [: ,0])
plt.xlabel('Time t')                                    # Label on the x-axis
plt.ylabel('Position theta')                            # Label on the y-axis
plt.grid ( True )
plt.savefig('RK4-figure.pdf')
plt.show()
