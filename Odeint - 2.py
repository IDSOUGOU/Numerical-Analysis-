# Resolution of differential equation n°2 by using the 'Odeint' method

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def   f  (Y, t):   
    g,a=9.8,3
    y,dy= Y                                  
    return   ( [ dy ,  -(3/4)*(g/a)*np.cos(y)] )
    
t = np.linspace (0. , 20 , 1000)
Y0 = [0. , 0.]            
sol1 = odeint (f, Y0, t)

# Graphical exploitation

plt.figure(1)                                     # Solution of differential equation
plt.plot(t, sol1[:,0], color='green')
plt.savefig('odeint-figure1.pdf')
plt.grid(True)                                    # Displaying a grid
plt.xlabel('Time t')                              # Label on the x-axis
plt.ylabel('Position teta')                       # Label on the y-axis
plt.title('Curious Oscillator n°2 -- Odeint --')

plt.figure(2)                                     # Phase portrait
plt.plot(sol1[:,0], sol1[:, 1],color ='red')
plt.savefig('odeint-figure2.pdf')
plt.grid(True)                                    # Displaying a grid
plt.xlabel('Position teta')                       # Label on the x-axis
plt.ylabel('Speed teta-prime')                    # Label on the y-axis
plt.title('Phase portrait')
plt.show()

