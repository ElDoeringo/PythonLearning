#Cirkel diagram
import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib
import numpy as np  # Import the NumPy library
name = ['Dog', 'Cat', 'Pig', 'Horse']
number = [10, 20, 30, 40]
plt.pie(number, labels=name)
plt.show()
