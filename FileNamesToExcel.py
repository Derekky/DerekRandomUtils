# This script retrieves all file names from a specified folder and saves them to an Excel file.
import os
import pandas as pd

def get_file_names_to_excel(folder_path, output_excel_path):
    # Get all file names in the folder
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Create a DataFrame from the file names
    df = pd.DataFrame(file_names, columns=["File Name"])
    
    # Save the DataFrame to an Excel file
    df.to_excel(output_excel_path, index=False)
    print(f"File names have been saved to {output_excel_path}")

# Example usage
if __name__ == "__main__":
    folder_path = r"C:\Users\username\Downloads"  # Replace with your folder path
    output_excel_path = r"C:\Users\username\Desktop\FileNames.xlsx"  # Replace with your desired output path
    get_file_names_to_excel(folder_path, output_excel_path)