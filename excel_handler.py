import pandas as pd

def read_excel_sheets(file_path):
    return pd.read_excel(file_path, sheet_name=None, engine='openpyxl')

def write_excel_sheets(sheets_dict, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for sheet_name, df in sheets_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
