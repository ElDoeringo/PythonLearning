#how and why are packages used
import Funktioner as f  # Imports the 'Funktioner' module and gives it the alias 'f'
import numpy as np      # Imports the NumPy library and gives it the alias 'np'

f.ligeTal(34)           # Calls the 'ligeTal' function from the 'Funktioner' module, passing 34 as the argument

s = [10, 20, 30, 40, 500]  # Creates a list 's' with the values [10, 20, 30, 40, 500]
print(np.sum(s))        # Calculates the sum of all elements in the list 's' using NumPy's 'sum' function and prints the result

