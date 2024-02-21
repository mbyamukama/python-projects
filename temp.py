import matplotlib
import matplotlib.pyplot as plt
import numpy as np


x=[11, 21, 33, 46, 78, 120, 34, 56, 88]
y=[27, 32, 40, 66, 65, 100, 20, 20, 100]

ex=ex2=ey=ey2=0;
n=len(x)
for i in  x:
    ex=ex+i
    ex2=ex+i**2
    
for i in  y:
    ey=ey+i
    ey2=ey+i**2
    
for i in range(n):
    exy=x[i]*y[i]

ux=ex/n
uy=ey/n  

covxy = exy-ux*uy;  
dx = (ex2-ux**2)**0.5
dy = (ey2-uy**2)**0.5

r=covxy/(dx*dy)

a=(ey*ex2-ex*exy)/(n*ex2-ux**2);
b=(uy-a)/ux


# Data for plotting
plt.scatter(x,y);
y = [a + b*i for i in x]



#fig, ax = plt.subplots()
#ax.plot(x, y)
#
#ax.set(xlabel='x (egg width)', ylabel='y (egg weight)',
#       title='relationship between x and y')
#ax.grid()
#
##fig.savefig("test.png")
plt.show()