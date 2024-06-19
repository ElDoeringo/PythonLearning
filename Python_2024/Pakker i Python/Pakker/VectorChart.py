import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib
import numpy as np  # Import the NumPy library

# Generate random data for the bar chart
data = np.random.randint(10, 50, size=5)

# Generate positions for the bars on the x-axis
plac = np.arange(len(data))

# Define the width of the bars
width = 0.35

# Create a bar chart with the random data
plt.bar(plac, data, width)

# Add labels, title, and grid
plt.xlabel('Position')  # Label for the x-axis
plt.ylabel('Value')  # Label for the y-axis
plt.title('Random Data Bar Chart')  # Title of the bar chart
plt.grid(True)  # Add a grid to the background of the plot

# Display the bar chart
plt.show()  # Render the plot in a window


#The script explained:
#import matplotlib.pyplot as plt  # Import the pyplot module from the matplotlib library for plotting
#import numpy as np  # Import the NumPy library for numerical operations
# matplotlib.pyplot is used for creating static, animated, and interactive visualizations in Python.
# numpy is a library for numerical operations, particularly useful for vectorized operations and working with arrays.

# Step 1: Generate random data for the bar chart
# Using np.random.randint to create an array of 5 random integers between 10 and 50

#data = np.random.randint(10, 50, size=5)

# Step 2: Generate positions for the bars on the x-axis
# np.arange(len(data)) creates an array of positions [0, 1, 2, 3, 4] for the bars on the x-axis.

#plac = np.arange(len(data))

# Step 3: Define the width of the bars
# This is a constant that determines how wide each bar will be

#width = 0.35

# Step 4: Create a bar chart with the random data
# plt.bar takes the positions (plac), the data (heights of the bars), and the width of each bar

#plt.bar(plac, data, width)

# Step 5: Add labels, title, and grid for better readability

#plt.xlabel('Position')  # Label for the x-axis
#plt.ylabel('Value')  # Label for the y-axis
#plt.title('Random Data Bar Chart')  # Title of the bar chart
#plt.grid(True)  # Add a grid to the background of the plot

# Step 6: Display the bar chart
#plt.show()  # Render the plot in a window
