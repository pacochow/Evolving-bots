import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
x = 0
y = 0
z = -0.5

a = 1
b = 1
c = 1
for i in range (10):
    z += 1
    a *= 0.9
    b *= 0.9
    c *= 0.9
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[a,b,c])
pyrosim.End()