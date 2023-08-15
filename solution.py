import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    
    def __init__(self, ID):
        self.weights = 2*np.random.rand(c.numSensorNeurons, c.numMotorNeurons)-1
        self.myID = ID
        
    def Start_Simulation(self, directOrGUI: str):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python3 simulate.py {directOrGUI} {str(self.myID)} 2&>1 &")
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{str(self.myID)}.txt"):
            time.sleep(0.1)
        f = open(f"fitness{str(self.myID)}.txt", "r")
        self.fitness = float(f.read())

        f.close()
    
        os.system(f"rm fitness{str(self.myID)}.txt")
        
        
    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons-1)
        column = random.randint(0, c.numMotorNeurons-1)
        self.weights[row, column] = random.random()*2-1
        
    def Set_ID(self, ID):
        self.myID = ID
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[3,0,0.5] , size=[1,1,1])
        pyrosim.End()
    
    
    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso", child = "BackLeg", type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])
        
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg", parent = "FrontLeg", child = "FrontLowerLeg", type = "revolute", position = [0, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name = "FrontLowerLeg", pos = [0, 0, -0.5], size = [0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg", parent = "BackLeg", child = "BackLowerLeg", type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name = "BackLowerLeg", pos = [0, 0, -0.5], size = [0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg", parent = "LeftLeg", child = "LeftLowerLeg", type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LeftLowerLeg", pos = [0, 0, -0.5], size = [0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg", parent = "RightLeg", child = "RightLowerLeg", type = "revolute", position = [1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "RightLowerLeg", pos = [0, 0, -0.5], size = [0.2, 0.2, 1])
        
        pyrosim.End()
        
    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        links = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg", "BackLowerLeg", "FrontLowerLeg", "LeftLowerLeg", "RightLowerLeg"]
        joints = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg", "BackLeg_BackLowerLeg", "FrontLeg_FrontLowerLeg", "LeftLeg_LeftLowerLeg", "RightLeg_RightLowerLeg"]
        for i in range(len(links)):
            pyrosim.Send_Sensor_Neuron(name = i , linkName = links[i])
        for i in range(len(joints)):
            pyrosim.Send_Motor_Neuron(name = i+len(links) , jointName = joints[i])

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName= currentRow, targetNeuronName= currentColumn+c.numSensorNeurons, weight =self.weights[currentRow][currentColumn])
        pyrosim.End()