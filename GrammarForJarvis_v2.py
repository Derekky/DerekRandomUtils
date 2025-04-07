#This code parses an Excel file with multiple sheets, extracts specific columns, and saves the data into a single CSV file.
#It also handles JSON formatting in a way that ensures compatibility with CSV format.
#This way a third-party application can first read the CSV file and then interpret the JSON inside it correctly.

import pandas as pd
import json

input_path = r"c:\Users\dersil\Desktop\grammar.xlsx"  # Update to the correct file path
output_path = r"c:\Users\dersil\Desktop\ADA.csv"  # Update to the desired output path

# Initialize an empty DataFrame to store all sheets
combined_df = pd.DataFrame()

excel_file = pd.ExcelFile(input_path)
sheet_names = excel_file.sheet_names  # List of all sheet names

for sheet_name in sheet_names:
    # Read the Excel file
    try:
        df = pd.read_excel(input_path, sheet_name=sheet_name)
        
        # Keep "text" and "grammar" columns as-is
        text_grammar_df = df[["text"]]
        
        # Create a new column with JSON objects from the specified columns
        if all(col in df.columns for col in ["response", "audio", "next_step", "finaliza_atendimento"]):
            # First escape correctly with multiple audio files in the same "audio" column
            df["audio"] = df["audio"].apply(lambda x: x.replace(',','","') if isinstance(x, str) else [])
            # Deal with empty values
            df["response"] = df["response"].apply(lambda x: x.replace('nan','""') if isinstance(x, str) else [])

            df['category'] = df.apply(lambda row: '"' + json.dumps({
            "response": [row["response"]],
            "audio": [row["audio"]],
            "next_step": row["next_step"],
            "finaliza_atendimento": row["finaliza_atendimento"]
            }, ensure_ascii=False).replace('"','""') 
            + '"', axis=1)
            
            # Combine "text", "grammar", and the new JSON column
            combined_sheet_df = pd.concat([text_grammar_df, df["category"]], axis=1)
            combined_sheet_df = pd.concat([combined_sheet_df, df[["grammar"]]], axis=1)
        else:
            # If the required columns for JSON are missing, only use "text" and "grammar"
            combined_sheet_df = text_grammar_df

        # Append the data to the combined DataFrame
        combined_df = pd.concat([combined_df, combined_sheet_df], ignore_index=True)
        print(f"Sheet '{sheet_name}' added to the combined DataFrame.")
    except Exception as e:
        print(f"Error processing sheet '{sheet_name}': {e}")

# Save the combined DataFrame to a single CSV file
combined_df.to_csv(output_path, index=False, quotechar="|", sep=';')

# Open the output CSV file and clean it
with open(output_path, 'r') as file:
    content = file.read()
content = content.replace("|", "").replace(";;", ";").replace("[NaN]", '').replace("NaN", '').replace("nan", '').replace('\\','').replace('[[]]','""""')
with open(output_path, 'w') as file:
    file.write(content)
    
print(f"All sheets saved to a single CSV file: {output_path}")