import openpyxl

invFile = openpyxl.load_workbook("inventory.xlsx")

productList = invFile['Sheet1']

numberLines = productList.max_row

print(numberLines)

for productRow in range(2,numberLines+1):
    print(productRow)
    