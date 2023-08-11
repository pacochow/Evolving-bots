import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy as np
import random
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    
    def __init__(self):
     
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
    
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_to_Act()
    

        
        
        
    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            time.sleep(1/2400)
            self.robot.Sense(i)
            self.robot.Act(i)

            
    def __del__(self):
        p.disconnect()