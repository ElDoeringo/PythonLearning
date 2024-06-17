import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib
import numpy as np  # Import the NumPy library
data = [20, 35, 30, 35, 27] # Define the data for the bar chart
plac = np.arange(len(data)) # Generate an array with the positions for the bars on the x-axis
width = 0.35 #Define the width of the bars # Create a bar chart with the data provided
plt.bar(plac, data, width) # Display the bar chart

#An array is a data structure that consists of a collection of elements, each identified by an array index or key. 
#The elements of an array are stored in contiguous memory locations, which allows for efficient access and modification of data.

#Key Characteristics of an Array:
#Fixed Size: Arrays have a fixed size that is determined at the time of their creation. The size cannot be changed once the array is created.
#Indexed Access: Each element in the array can be accessed using an index, which typically starts at 0.
#Homogeneous Elements: Arrays usually store elements of the same data type, which ensures that each element occupies the same amount of memory.

#Example in Python:
#In Python, arrays can be implemented using the list data type, which is more flexible as it can grow dynamically and hold elements of different data types. However, for fixed-size, homogeneous collections, the array module or libraries like NumPy are more appropriate.

#Using a List:
#python
#Copy code
# Creating a list in Python
#my_list = [1, 2, 3, 4, 5]

# Accessing elements by index
#print(my_list[0])  # Output: 1
#print(my_list[2])  # Output: 3

# Modifying an element
#my_list[1] = 20
#print(my_list)  # Output: [1, 20, 3, 4, 5]
#Using the array Module:
#python
#Copy code
#import array

# Creating an array of integers
#my_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements by index
#print(my_array[0])  # Output: 1
#print(my_array[2])  # Output: 3

# Modifying an element
#my_array[1] = 20
#print(my_array)  # Output: array('i', [1, 20, 3, 4, 5])
#Advantages of Arrays:
#Fast Access: Accessing any element by index is very fast (O(1) time complexity).
#emory Efficiency: Arrays can be more memory-efficient compared to other data structures like linked lists, especially for large datasets.
#Disadvantages of Arrays:
#Fixed Size: Once an array is created, its size cannot be changed, which can lead to wasted space or the need for a new array if more space is required.
#Insertion/Deletion: Inserting or deleting elements (except at the end) can be costly because it may require shifting other elements.

