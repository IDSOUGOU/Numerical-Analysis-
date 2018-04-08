# A comparison of the resolution: RK4 and the harmonic solution of y "+ w²y = 0"
import matplotlib.pyplot as plt
import numpy as np

def rk4 ( f ,X0 , t ):                        
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

def s (Y , t ):                                         # Exact solution
        y,dy = Y
        k,m,g = 94,1,9.8
        return ( np.array([dy,(-1/(1+4*y**(2)))*(4*y*dy*dy + 2*(k/m)*(y**(3)) + 2*g*y ) ] ))
            
def g (Y , t ):                                         # Harmonic solution : y"+ w²y = 0
        k,m =94,1
        y,dy= Y 
        W = k/(4*m)                                     #  W= w*w = k/(4*m)
        return ( np.array([dy, -W*y ] ))                # Y(t) = A cos(w*t) with A = sqrt(0.25-2*g*m/k) = 0.203 m  
 
t = np . linspace (0 ,10 ,1000)                         # cutting the interval [0, 10] to 1000
ci = np . array ([0.203,0])                             # initial conditions (y(0) , y′(0)) = (0.203 , 0)  


sol1 = rk4 (s , ci , t )                                # Exact solution with RK4
sol2 = rk4 (g , ci , t )                                # Harmonic solution with  RK4

# Graphical exploitation
plt.figure(9)                  
plt.plot (t , sol1 [: ,0], color='green',label='Exact solution')
plt.plot (t , sol2 [: ,0], color='red',label='Harmonic solution')
plt.savefig('Curious Oscillator n°1-figure1.pdf')
plt.legend(loc = 'upper left')
plt.grid(True)                                          # Displaying a grid
plt.xlabel('Time t')                                    # Label on the x-axis
plt.ylabel('Position x')                                # Label on the y-axis
plt.title('Curious Oscillator n°1 ')
plt.show()