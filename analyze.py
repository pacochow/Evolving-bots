import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
plt.plot(backLegSensorValues, label = "Back leg")
plt.plot(frontLegSensorValues, label = "Front leg")
plt.legend()
plt.show()