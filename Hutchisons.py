from TransformationTransformer import Affine, Hutchison, shear, rotate, scale
import numpy as np

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

probVec2 = [1, 0, 0, 0]
affineList2 = [b1, b2, b3, b4]

# Dragon Curve
c1 = Affine(1 / np.sqrt(2) * np.cos(np.pi/4) , 1 / np.sqrt(2) * np.sin(np.pi/4), -1 / np.sqrt(2) * np.sin(np.pi/4), 1 / np.sqrt(2) * np.cos(np.pi/4),0,0)  # scaling 1/sqrt(2), rotation 45
c2 = Affine(1 / np.sqrt(2) * np.cos(3*np.pi/4) , 1 / np.sqrt(2) * np.sin(3*np.pi/4), -1 / np.sqrt(2) * np.sin(3*np.pi/4), 1 / np.sqrt(2) * np.cos(3*np.pi/4),1,0)  # scaling 1/sqrt(2), rotation 135

probVec3 = [0.5, 0.5]
affineList3 = [c1, c2]


# Initialize each Hutchison
h1 = Hutchison(affineList1, probVec1)
h2 = Hutchison(affineList2, probVec2)
h3 = Hutchison(affineList3, probVec3)

presets = {
    "Barnsley": h1,
    "Tree": h2,
    "Dragon": h3
    }

