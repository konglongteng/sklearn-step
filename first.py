from numpy import *
#print random.rand(4,4)
randMat = mat(random.rand(4,4))
print randMat
randN = randMat.I
print randN

theE = randN * randMat
print theE



