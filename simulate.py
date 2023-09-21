import pybullet as p
import pyrosim.pyrosim as pyrosim
from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGui, solutionID)
simulation.Run()
simulation.Get_Fitness()


