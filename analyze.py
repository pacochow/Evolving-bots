import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAngles = np.load("data/targetAngles.npy")
plt.plot(targetAngles)
# plt.plot(backLegSensorValues, label = "Back leg")
# plt.plot(frontLegSensorValues, label = "Front leg")
# plt.legend()
plt.show()