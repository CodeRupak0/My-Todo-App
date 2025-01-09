import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

def solve_beam (l1, l2, w1, w2):
    l=l1+l2  #total length of beam
    Mx= sp.symbols('Mx')
    Mx= sp.solveset(Mx*l1/3+w1*l1**3/24+Mx*l2/3+w2*l2**3/24,Mx).args[0]
        #solve to find the value of moment
    Va, Vb1, Vb2, Vc=sp.symbols('Va Vb1 Vb2 Vc')
    Va, Vb1=sp.linsolve([Va+Vb1-w1*l1,Vb1*l1-w1*l1**2/2+Mx],(Va, Vb1)).args[0]
    Vc, Vb2 = sp.linsolve([Vb2 + Vc - w2 * l2, Vb2 * l2 + w2 * l2 ** 2 / 2 + Mx], (Vc, Vb2)).args[0]
        # solving linear equations to find the values of Va, Vb1, Vb2 and Vc.
    Vb=Vb1+Vb2

    x1=np.arange(0,l1+0.1,0.1)         #for first beam
    x2=np.arange(0,l2+0.1,0.1)         #for second beam
        # creating array of beam length in X-axis with step 0.1
    beam1= pd.DataFrame({"x": x1})
    beam2 = pd.DataFrame({"x": x2})
    beam1["M"]=Va*beam1.x-(w1*beam1.x**2)/2       # calculating moment for first beam
    beam2["M"] =Mx+ Vb2 * beam2.x - (w2*beam2.x ** 2 )/ 2

    beam1["V"]= Va-w1*beam1.x
    beam2["V"] = Vb2 - w2 * beam2.x

    beam2.x = beam2.x +l1     # as beam 2 starts with zero, adding l1 to make the beam continuous with first beam.
    beam = pd.concat(beam1,beam2)

    return (beam)
#display(beamcalc())

header=pd.MultiIndex.from_tuples([("Combo 1","M"),("Combo 1","V"),("Combo 2","M"),("Combo 2","V")])
combos=pd.DataFrame(columns=header)
combos["x"]= solve_beam(4,5,3.2,4.5)["x"]
combos["Combo 1"]= solve_beam(4,5,3.2,4.5)
combos["Combo 2"]= solve_beam(4,5,4.5,3.2)
combos=combos.set_index("x")

combos=combos.astype("float")
combos.head()

fig= plt.figure(figsize=(10,6))
ax=plt.subplot(211)
ax.invert_yaxis()

combos.loc[:,pd.IndexSlice[:,"M"]].plot(ax=ax)

ax=plt.subplot(212)
ax.invert_yaxis()

combos.loc[:,pd.IndexSlice[:,"V"]].plot(ax=ax)


"""l1= int(input("Enter the length of 1st portion of beam"))
l2= int(input("Enter the length of 2nd portion of beam"))
w1= int(input("Enter the Load Intensity (UDL) of 1st portion of beam"))
w2= int(input("Enter the Load Intensity (UDL) of 2nd portion of beam"))

beam= beamcalc (l1, l2, w1, w2)
"""
