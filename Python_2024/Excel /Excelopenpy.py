import openpyxl as xl  # Import the openpyxl library as xl for working with Excel files

wb = xl.load_workbook('/this PC/Desktop/Timeseddel.xlsx')  # Load the workbook named 'Timeseddel.xlsx'
print(wb.sheetnames) # Print the names of all the sheets in the workbook
