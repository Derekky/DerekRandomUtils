# Old code to convert multiple sheets of an Excel file into a single CSV file.
# It is more straightforward than v2

import pandas as pd

input_path = r"c:\Users\username\Desktop\grammar.xlsx"  # Update to the correct file path
output_path = r"c:\Users\username\Desktop\grammar.csv"  # Update to the desired output path

# Initialize an empty DataFrame to store all sheets
combined_df = pd.DataFrame()

excel_file = pd.ExcelFile(input_path)
sheet_names = excel_file.sheet_names  # List of all sheet names

for sheet_name in sheet_names:
    # Read the Excel file
    try:
        df = pd.read_excel(input_path, sheet_name=sheet_name)
        # Select only the first three columns: "text", "grammar", and "category"
        df = df[["text", "category", "grammar"]]
        # Append the data to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)
        print(f"Sheet '{sheet_name}' added to the combined DataFrame.")
    except Exception as e:
        print(f"Error processing sheet '{sheet_name}': {e}")

# Save the combined DataFrame to a single CSV file
combined_df.to_csv(output_path, index=False, quotechar="|", sep=';')

# Open the output CSV file and clean it
with open(output_path, 'r') as file:
    content = file.read()
content = content.replace("|", "").replace(";;", ";") #The second replace was specific to a certain use case
with open(output_path, 'w') as file:
    file.write(content)
    
print(f"All sheets saved to a single CSV file: {output_path}")