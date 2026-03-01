import pandas as pd
import os

# JSON file path
json_file = "/Users/shamsher/Desktop/Project/python_crash_course/DATAS/departments.json"

# Check if file exists
if not os.path.exists(json_file):
    print("❌ JSON file not found. Run connect.py first.")
    exit()

# Read JSON
df = pd.read_json(json_file)

# Generate Excel file
excel_file = "/Users/shamsher/Desktop/Project/python_crash_course/DATAS/departments.xlsx"
df.to_excel(excel_file, index=False)

print(f"✅ Excel file created: {excel_file}")