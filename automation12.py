import openpyxl as xl

# used to load the workbook
wb = xl.load_workbook('transactions-forpyautomation.xlsx')

sheet = wb['Sheet1']
# accessed the sheet 1 for the excel file

# cell = sheet['a1']
# we are definning the cell 
cell = sheet.cell(1,1) 
# better method to get the cell(row,column)

print(cell.value)