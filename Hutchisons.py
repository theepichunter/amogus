from TransformationTransformer import Affine, Hutchison, shear, rotate, scale
import numpy as np
import math
# Barnsley
a1 = Affine(0, 0, 0, 0.16, 0, 0)
a2 = Affine(0.85, 0.04, -0.04, 0.85, 0, 1.6)
a3 = Affine(0.2, -0.26, 0.23, 0.22, 0, 1.6)
a4 = Affine(-0.15, 0.28, 0.26, 0.24, 0, 0.44)

probVec1 = [0.01, 0.85, 0.07, 0.07]
affineList1 = [a1, a2, a3, a4]

# Tree
b1 = Affine(0, 0, 0, 0.5, 0, 0)
b2 = Affine(0.42, -0.42, 0.42, 0.42, 0, 0.2)
b3 = Affine(0.42, 0.42, -0.42, 0.42, 0, 0.2)
b4 = Affine(0.1, 0, 0, 0.1, 0, 0.2)

probVec2 = [0.01, 0.85, 0.07, 0.07]
affineList2 = [b1, b2, b3, b4]

# Dragon Curve
c1 = Affine(1 / np.sqrt(2) * np.cos(np.pi/4) , 1 / np.sqrt(2) * np.sin(np.pi/4), -1 / np.sqrt(2) * np.sin(np.pi/4), 1 / np.sqrt(2) * np.cos(np.pi/4),0,0)  # scaling 1/sqrt(2), rotation 45
c2 = Affine(1 / np.sqrt(2) * np.cos(3*np.pi/4) , 1 / np.sqrt(2) * np.sin(3*np.pi/4), -1 / np.sqrt(2) * np.sin(3*np.pi/4), 1 / np.sqrt(2) * np.cos(3*np.pi/4),1,0)  # scaling 1/sqrt(2), rotation 135

probVec3 = [0.5, 0.5]
affineList3 = [c1, c2]

# Serpenski Triangle
A = [50,0]
B = [-50,0]
C = [0,87]
d1 = Affine(0.5, 0, 0, 0.5, A[0]/2, A[1]/2)
d2 = Affine(0.5, 0, 0, 0.5, B[0]/2, B[1]/2)
d3 = Affine(0.5, 0, 0, 0.5, C[0]/2, C[1]/2)
probVec4 = [.33, .33, .33]
affineList4 = [d1, d2, d3]

# square
A = [50,0]
B = [-50,0]
C = [50,50]
D = [-50, 50]
affineList5 = [Affine(0.5, 0, 0, 0.5, A[0]/2, A[1]/2), Affine(0.5, 0, 0, 0.5, B[0]/2, B[1]/2), Affine(0.5, 0, 0, 0.5, C[0]/2, C[1]/2), Affine(0.5, 0, 0, 0.5, D[0]/2, D[1]/2)]
probVec5 = [.25, .25, .25, .25]

# Pentagon
A = [28.82-30, -1.63+60]
B = [31.18-30, -1.63+60]
C = [31.91-30, 0.62+60]
D = [30-30, 2.01+60]
E = [28.09-30, 0.62+60]
affineList6 = [Affine(0.5, 0, 0, 0.5, A[0]/2, A[1]/2), Affine(0.5, 0, 0, 0.5, B[0]/2, B[1]/2), Affine(0.5, 0, 0, 0.5, C[0]/2, C[1]/2), Affine(0.5, 0, 0, 0.5, D[0]/2, D[1]/2), Affine(0.5, 0, 0, 0.5, E[0]/2, E[1]/2)]
probVec6 = [.2, .2, .2, .2, .2]

#Coral
A= Affine(-0.16666667, -0.1666667,  0.16666667, -0.1666667,   0.0000000,  0.000000)
B=Affine(0.83333333,  0.2500000, -0.25000000,  0.8333333, -0.1666667, -0.166667)
C=Affine(0.33333333, -0.0833333,  0.08333333,  0.3333333,    0.0833333,  0.666667)
affineList7 = [A, B, C]
probVec7 = [0.163,0.600,0.237]

#Sigma
A= Affine(0.5,   0.5,  -0.5,   0.5,   0.0 ,  0.0,)
B = Affine(0.5,  -0.5,   0.5,   0.5,   0.5,  -0.5)
affineList8 = [A,B]
probVec8 =[.5, .5]

#Menger
affineList9= [Affine(0.333333, 0, 0, 0.333333, 0.000000, 0.000000),
Affine(0.333333, 0, 0, 0.333333, 0.333333, 0.000000),
Affine(0.333333, 0 ,0, 0.333333, 0.666667, 0.000000),
Affine(0.333333, 0, 0,0.333333, 0.000000, 0.333333),
Affine(0.333333, 0, 0, 0.333333, 0.000000, 0.666667)]
probVec9 = [0.125, 0.125, 0.125, 0.125, 0.125]

#Tower
affineList10=[Affine(0.75,  0.00,   0.00,   0.30,  -0.20,   0.00) ,
Affine(0.75,  0.00,   0.00 ,  0.30,   0.20,   0.00) ,
Affine(0.50 , 0.00,   0.00,   0.80,   0.00,   0.20)  ]
probVec10=[.23, .23, .54]

#Tree2

affineList11=[Affine(0.195,  -0.488,   0.344,   0.443,   0.722,   0.536) ,
Affine(0.462,   0.414,  -0.252,   0.361,   0.538,   1.167)  ,
Affine(-0.058,  -0.070 ,  0.453,  -0.111,   1.125 ,  0.185),
Affine(-0.045 ,  0.091,  -0.469 , -0.022,   0.863 ,  0.871) ]
probVec11=[.4,.4,.1,.1]
# Initialize each Hutchison
h1 = Hutchison(affineList1, probVec1)
h2 = Hutchison(affineList2, probVec2)
h3 = Hutchison(affineList3, probVec3)
h4 = Hutchison(affineList4, probVec4)
h5 = Hutchison(affineList5, probVec5)
h6 = Hutchison(affineList6, probVec6)
h7 = Hutchison(affineList7, probVec7)
h8 = Hutchison(affineList8, probVec8)
h9 = Hutchison(affineList9, probVec9)
h10 = Hutchison(affineList10, probVec10)
h11 = Hutchison(affineList11, probVec11)
presets = {
    "Barnsley": h1,
    "Tree": h2,
    "Dragon": h3,
    "Serpenski": h4,
    "Square": h5,
    "Pentagon": h6,
    "Coral":h7,
    "Sigma": h8,
    "Menger": h9,
    "Tower": h10,
    "Tree2": h11
    }
