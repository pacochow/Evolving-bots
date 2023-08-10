import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
x = 0
y = 0
z = 1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[1,2,3])
pyrosim.End()