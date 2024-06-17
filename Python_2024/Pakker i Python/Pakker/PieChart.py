#Cirkel diagram
import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib
import numpy as np  # Import the NumPy library
name = ['Dog', 'Cat', 'Pig', 'Horse'] # Names of the categories in the pie chart
number = [10, 20, 30, 40] # Data for each category (make sure the numbers are correct)
plt.pie(number, labels=name) # Plot the pie chart with the provided data and labels
plt.show() # Display the pie chart

#Further explanation

#Import Statements:
#import matplotlib.pyplot as plt: This imports the pyplot module from the matplotlib library, which is commonly used for creating static, animated, and interactive visualizations in Python.
#import numpy as np: This imports the numpy library, which is used for numerical operations. While numpy is not explicitly used in this script, it's often used in conjunction with matplotlib.

#Variables:
#name = ['Hund', 'Kat', 'Gris', 'Hest']: This list contains the labels for each slice of the pie chart. Here, we have four categories: 'Hund', 'Kat', 'Gris', and 'Hest'.
#number = [10, 20, 30, 40]: This list contains the data values corresponding to each label. Each number represents the size of the pie slice for the respective category. Corrected the typo by removing the extra period.

#Plotting the Pie Chart:
#plt.pie(number, labels=name): This function call creates a pie chart with the number list determining the size of each slice and the name list providing the labels for each slice.

#Displaying the Plot:
#plt.show(): This function displays the pie chart in a new window. Without this call, the plot will not be rendered.