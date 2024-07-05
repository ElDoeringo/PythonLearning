import openpyxl as xl  # Import the openpyxl library as xl for working with Excel files

# Load the workbook named 'Timesheet.xlsx'
wb = xl.load_workbook('/workspaces/PythonLearning/Python_2024/Excel/Timesheet.xlsx')


# Access the first sheet in the workbook
sheet = wb[wb.sheetnames[0]]
sheet = wb.active
print(sheet["A1"].value)
print(sheet['A3'].value)

