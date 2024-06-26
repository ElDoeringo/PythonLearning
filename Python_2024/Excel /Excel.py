import openpyxl as xl  # Import the openpyxl library as xl for working with Excel files

# Define the full path to the Excel file
file_path = r'C:\Users\thdj\OneDrive - Implement\Desktop\Forca\Timesheet_Forca_2023.xlsx'  # Use raw string to avoid escape issues
  # Use raw string to avoid escape issues # Replace with the actual path to your file

try:
    # Load the workbook from the specified file path
    wb = xl.load_workbook(file_path)
    
    # Print the names of all the sheets in the workbook
    print(wb.sheetnames)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except xl.utils.exceptions.InvalidFileException:
    print(f"Error: The file '{file_path}' is not a valid Excel file or is corrupted.")
    
    
    
