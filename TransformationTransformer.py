import numpy as np


class Affine:

    def __init__(self, a, b, c, d, e, f):
        self.contraction = np.mat([[a, b], [c, d]])
        self.translate = np.mat([e, f])


class Hutchison:

    def __init__(self, affineList, probVec):
        self.affineList = affineList
        self.probVec = probVec

    def getProbAcc(self):
        cache = 0
        probAcc = [0]
        for i in range(len(self.probVec)):
            cache += self.probVec[i]
            probAcc.append(cache)
        return probAcc

    def getLength(self):
        return len(self.affineList)


def rotate(hutchison, theta, lower, upper):
    rotation = ([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
    for i in range(lower, upper):
        hutchison.affineList[i].contraction = np.matmul(hutchison.affineList[i].contraction, rotation)

def shear(hutchison, shear_fac, lower, upper):
    shear = ( [[1, shear_fac] , [0,1]] )
    for i in range(lower, upper):
        hutchison.affineList[i].contraction = np.matmul(hutchison.affineList[i].contraction, shear)

def scale(hutchison, scale_fac, lower, upper):
    scale = ( [[scale_fac , 0] , [0,scale_fac]] )
    for i in range(lower, upper):
        hutchison.affineList[i].contraction = np.matmul(hutchison.affineList[i].contraction, scale)



