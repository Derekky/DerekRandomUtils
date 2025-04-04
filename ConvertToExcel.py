# Code to convert a text table into an Excel spreadsheet
# Only supports tables in the specific style or similar to the provided example

import pandas as pd
import re
import os

def parse_table(text):
    lines = text.strip().split("\n")
    data = []
    
    for line in lines:
        # Remove table borders
        if re.match(r'^[|=`\-=]+$', line.strip()):
            continue
        
        # Remove side borders and split the fields
        row = [col.strip() for col in re.split(r'\s{2,}|\|', line) if col.strip()]
        if row:  # Add only non-empty rows
            data.append(row)
    
    return data

def save_to_excel(data, filename="output.xlsx"):
    try:
        # Get the desktop path
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        full_path = os.path.join(desktop_path, filename)
        
        df = pd.DataFrame(data[1:], columns=data[0])  # Use the first row as the header
        df.to_excel(full_path, index=False)
        print(f"File saved as {full_path}")
    except Exception as e:
        print(f"Error saving the file: {e}")

# Table text
table_text = """
       |================================================================|
       | Sum/Avg|  956  11667 | 85.4    9.7    4.9    3.8   18.4   67.2 |
       |================================================================|
       |  Mean  |  1.0   12.2 | 83.8   10.1    6.1    4.3   20.5   67.2 |
       |  S.D.  |  0.0   14.1 | 19.3   13.7   12.8   14.2   24.6   47.0 |
       | Median |  1.0    7.0 | 90.0    4.1    0.0    0.0   13.3  100.0 |
"""

data = parse_table(table_text)
if data:
    save_to_excel(data)
else:
    print("Error: No data was extracted from the table.")
