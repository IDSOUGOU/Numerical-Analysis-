# Comparison of the resolution: RK4, Odeint and Euler of y" + k * cos (y) = 0 

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def euler ( f ,X0 , t ):
    n = len (t)
    X = np . zeros ((n ,)+ np . shape ( X0 ))
    X [0]= X0
    for i in range (n -1):
        h =( t [ i +1] - t[ i ])
        X [ i +1]= X [ i ]+ f ( X [i ] , t[ i ])* h
    return X

def rk4 ( f ,X0 , t ):                                 # Runge Kutta - order 4
    n = len (t )
    X = np . zeros ((n,) + np.shape(X0))               
    X [0]= X0                                         
    for i in range (n -1):
        k1 = f ( X[ i ] ,t [ i ])                      
        h = (t [i +1] - t [ i ])/2
        k2 = f (X [ i ]+ h * k1 , t [i ]+ h)
        k3 = f (X [ i ]+ h * k2 , t [i ]+ h)
        k4 = f (X [ i ]+2* h* k3 ,t [ i ]+2* h )
        X [i +1]= X [i ]+ h /3*( k1 +2* k2 +2* k3 + k4 )
    return X
    
def g (Y , t ):
        y,dy = Y
        return ( np.array([dy,-(3/4)*(9.8/3)*np.cos( y) ] ))
    
t = np.linspace (0. , 20 , 1000)
Y0 = [0. , 0.]     
# Solution of the differential equation by the 3 methods
sol1 = odeint (g, Y0, t)
sol2 = rk4 (g , ci , t )
sol3 = euler (g , ci , t )

# Graphical comparison of the resolution: RK4, Odeint and Euler of y" + k * cos (y) = 0 

plt.figure(5)                  
plt.plot (t , sol1 [: ,0], color='green',label='Odeint')
plt.plot (t , sol2 [: ,0], color='red',label='RK4')
plt.plot (t , sol3 [: ,0], color='blue',label='Euler')
plt.savefig('odeint-figure1.pdf')
plt.legend(loc = 'upper left')
plt.grid(True)                         #  Displaying a grid
plt.xlabel('Time t')                   #  Label on the x-axis
plt.ylabel('Position teta')            #  Label on the y-axis
plt.title('Curious Oscillator n°2 ')
plt.show()