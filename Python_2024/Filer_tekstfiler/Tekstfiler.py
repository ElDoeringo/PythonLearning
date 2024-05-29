#with open('Text.txt', 'r') as lo: # Opens the file Lorem.txt in read mode
 ##  content = lo.read()          # Reads the entire content of the file
   # print(content)               # Prints the content of the file
    #lo.close()                   # Closes the file

import os  # Import the os module to interact with the operating system

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the script and then get its directory

# Construct the full path to the file
file_path = os.path.join(script_dir, 'Lorem.txt')  # Combine the script directory and the file name to get the full file path

# Check if the file exists
if os.path.exists(file_path):  # Check if the file exists at the constructed path
    # Open and read the file
    with open(file_path, 'r') as lo:  # Open the file in read mode and assign it to the variable 'lo'
        print(f"File '{lo.name}' found and opened successfully.")  # Print the name of the file to confirm it is opened
        content = lo.read()  # Read the entire content of the file
        print("File content:")  # Print a message indicating the file content will be displayed
        print(content)  # Print the actual content of the file
else:
    print(f"The file '{file_path}' does not exist.")  # Print a message indicating the file was not found