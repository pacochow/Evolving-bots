import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import pybullet as p

class MOTOR:
    
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.phaseOffset = c.phaseOffset
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.frequency/2
        self.motorValues = np.zeros(c.iterations)

    def Set_Value(self, robotId, t):
        self.motorValues[t] = pyrosim.Set_Motor_For_Joint(

                    bodyIndex = robotId,

                    jointName = self.jointName,

                    controlMode = p.POSITION_CONTROL,

                    targetPosition = self.amplitude*np.sin(self.frequency*t + self.phaseOffset),

                    maxForce = 50)
        
    def Save_Values(self):
        np.save(f"data/{self.jointName}.npy", self.motorValues)