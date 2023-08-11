import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy as np
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

iterations = 1000
BackLeg_amplitude = np.pi/4
BackLeg_frequency = 0.05
BackLeg_phaseOffset = 0

FrontLeg_amplitude = np.pi/4
FrontLeg_frequency = 0.05
FrontLeg_phaseOffset = np.pi/4

backLegSensorValues = np.zeros(iterations)
frontLegSensorValues = np.zeros(iterations)

for i in range(iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = "Torso_BackLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition = BackLeg_amplitude*np.sin(BackLeg_frequency*i + BackLeg_phaseOffset),

        maxForce = 50)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = "Torso_FrontLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition = FrontLeg_amplitude*np.sin(FrontLeg_frequency*i + FrontLeg_phaseOffset),

        maxForce = 50)
    time.sleep(1/2400)

p.disconnect()
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# np.save("data/targetAngles.npy", targetAngles)