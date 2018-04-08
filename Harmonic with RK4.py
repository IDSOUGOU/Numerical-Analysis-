# Resolution of differential equation n°1 by using the 'RK4' method

import matplotlib.pyplot as plt
import numpy as np


def rk4 ( f ,X0 , t ):                                 # Runge Kutta - order 4
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
        X [i +1]= X [i ]+ h /3*( k1 +2* k2 +2* k3 + k4 )# We have already divided h by 2
    return X
    
def g (Y , t ):
        k,m =94,1
        y,dy= Y 
        W= k/(4*m)                                      #  W= w*w = k/(4*m)
        return ( np.array([dy,-W*y ] ))                 
 
t = np . linspace (0 ,10 ,1000)                         # cutting the interval [0, 10] to 1000
ci = np . array ([0.05,0])                              # initial conditions (y(0) , y′(0)) = (0.05 , 0)
sol2 = rk4 (g , ci , t )                                # solution by using RK4

# Variation of position over time 
plt.figure (3)
plt.title ( 'Harmonic Oscillator y"+ w²y = 0 -- RK4 -- ' )
plt.plot (t , sol2 [: ,0])
plt.xlabel('Time t')                                    # Label on the x-axis
plt.ylabel('Position x')                                # Label on the y-axis
plt.grid ( True )
plt.savefig('RK4-figure.pdf')
plt.show()
