import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        
    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)
            
            if t == c.iterations - 1:
                self.sensors[sensor].Save_Values()
        
    def Prepare_to_Act(self):
        
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        
    def Act(self, t):
        for motor in self.motors:
            self.motors[motor].Set_Value(self.robotId, t)
            
            if t == c.iterations - 1:
                self.motors[motor].Save_Values()
        