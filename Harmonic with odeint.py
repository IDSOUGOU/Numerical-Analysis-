# Resolution of differential equation n°1 by using the 'Odeint' method

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def   f  (Y, t):   
    k,m =94,1
    y,dy= Y 
    W= k/(4*m)                               #  W= w*w = k/(4*m)                   
    return   ( [ dy , -W*y] )
    
t = np.linspace (0. , 10 , 1000)
Y0 = [0.05 , 0.]            
sol1 = odeint (f, Y0, t)

#  Graphical exploitation
plt.figure(1)                                #  Solution of differential equation
plt.plot(t, sol1[:,0], color='green')
plt.savefig('odeint-figure1.pdf')
plt.grid(True)                               #  Displaying a grid
plt.xlabel('Time t')                         #  Label on the x-axis
plt.ylabel('Position x')                     #  Label on the y-axis
plt.title('Harmonic Oscillator y"+ w²y = 0  -- Odeint --')

plt.figure(2)                                #  Phase portrait
plt.plot(sol1[:,0], sol1[:, 1],color ='red')
plt.savefig('odeint-figure2.pdf')
plt.grid(True)                               #  Displaying a grid
plt.xlabel(" Position x ")                   #  Label on the x-axis
plt.ylabel(" Speed x' ")                     #  Label on the y-axis
plt.title('Phase portrait')
plt.show()