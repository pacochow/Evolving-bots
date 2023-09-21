import numpy as np
from solution import SOLUTION

weights = np.load("best_model.npy")

solution = SOLUTION(0)
solution.weights = weights
solution.Start_Simulation("GUI")
solution.Wait_For_Simulation_To_End