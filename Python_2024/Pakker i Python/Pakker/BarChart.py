import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib
import numpy as np  # Import the NumPy library
data = [20, 35, 30, 35, 27]
plac = np.arange(len(data))
width = 0.35
plt.bar(plac, data, width)