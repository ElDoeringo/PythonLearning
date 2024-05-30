import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib
import numpy as np  # Import the NumPy library

# Funktion der skal plottes (Function to be plotted)
def f(x):
    return np.exp(-x) * np.cos(2 * np.pi * x)  # Exponential decay multiplied by cosine function

x1 = np.arange(0.0, 5.0, 0.1)  # Generate values from 0.0 to 5.0 with a step of 0.1
x2 = np.arange(0.0, 5.0, 0.02)  # Generate values from 0.0 to 5.0 with a step of 0.02

# Den plottede figur (The plotted figure)
plt.figure()  # Create a new figure
plt.subplot(2, 1, 1)  # Create a subplot with 2 rows and 1 column, and select the 1st subplot
plt.plot(x1, f(x1), color='red', marker='o')  # Plot x1 and f(x1) with red color and circle markers
plt.plot(x2, f(x2), 'b')  # Plot x2 and f(x2) with blue color
plt.show()  # Display the plot
