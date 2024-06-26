import openpyxl as xl  # Import the openpyxl library as xl for working with Excel files

wb = xl.load_workbook('Timeseddel.xlsx')  # Load the workbook named 'Timeseddel.xlsx'

sheet = wb[wb.sheetnames[0]] #selects the first Excel sheet 
print(sheet.title) # Print the name of the specific sheet in the workbook