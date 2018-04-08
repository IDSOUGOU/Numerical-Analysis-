# Resolution of differential equation n°2 by using the 'Euler' method

import matplotlib.pyplot as plt
import numpy as np


def euler ( f ,X0 , t ):
    n = len (t)
    X = np . zeros ((n ,)+ np . shape ( X0 ))
    X [0]= X0
    for i in range (n -1):
        h =( t [ i +1] - t[ i ])
        X [ i +1]= X [ i ]+ f ( X [i ] , t[ i ])* h
    return X
    
def g (Y , t ):
        y,dy = Y
        return ( np.array([dy,-(3/4)*(9.8/3)*np.cos( y) ] ))
        
t = np . linspace (0 ,20 ,1000)                         # cutting the interval [0, 20] to 1000
ci = np . array ([0,0])                                 # initial conditions  (y(0) , y′(0)) = (0 , 0)
sol3 = euler (g , ci , t )                              # solution by using Euler

# Variation of tetha over time  
plt.figure (4)
plt.title ( " Curious Oscillator n°2 -- Euler -- " )
plt.plot (t , sol3 [: ,0])
plt.xlabel('Time t')                                   # Label on the x-axis
plt.ylabel('Position theta')                           # Label on the y-axis
plt.grid ( True )
plt.savefig('Euler-figure.pdf')
plt.show()