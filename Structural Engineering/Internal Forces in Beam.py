import numpy as np
from matplotlib import pyplot as pt
L= 4  #m - Length of Beam
w= 25 #KN/m - applied load in the form of UDL

x= np.linspace(0,L,20)
BM=w/2*(L*x-x**2)
SF=w*(L/2-x)

pt.figure(figsize=(8,4))
pt.plot([0]*len(x), color='k')
pt.plot(-BM)
pt.plot(SF)
pt.show()
