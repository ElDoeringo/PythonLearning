#Cirkel diagram
import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib
import numpy as np  # Import the NumPy library
name = ['Dog', 'Cat', 'Pig', 'Horse'] # Names of the categories in the pie chart
number = [10, 20, 30, 40] # Data for each category (make sure the numbers are correct)
plt.pie(number, labels=name) # Plot the pie chart with the provided data and labels
plt.show() # Display the pie chart
