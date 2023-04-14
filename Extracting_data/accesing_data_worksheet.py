
from openpyxl import load_workbook

data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'

## Load the entire workbook

wb = load_workbook(data_file, data_only = True)

## Load one worksheet

ws = wb['2013-2019 Killings by State']
all_rows = list(ws.rows)


## Accessing Data in a Worksheet

# print(f"Found {len(all_rows)} rows of data")

# print("\nFirst rows of data:")
# for row in all_rows[:5]:
# 	print(row)

## Accessing Data from Cells

# for cell in all_rows[0]:
# 	print(cell.value)


## Extracting Data from Specific Cells
## Pull information from specific cells

for row in all_rows[1:52]:
	state = row[0].value
	percent_aa = int(round(row[3].value, 2)* 100)
	percent_aa_victims = int(round(row[4].value, 2)* 100)

	print(f"\n{state}")
	print(f"{percent_aa}% of residents are African American")
	print(f"{percent_aa_victims}% killed by police were African American")





