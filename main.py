from config import INPUT_FILE, TARGET_LANGUAGE, TRANSLATOR
import os
from excel_handler import read_excel_sheets, write_excel_sheets
from translator import translate_dataframe

def main():
    print(f"Selected translator: {TRANSLATOR}")
    print("Reading Excel file...")
    sheets = read_excel_sheets(INPUT_FILE)

    print("Translating sheets...")
    translated_sheets = {}
    for name, df in sheets.items():
        print(f"Translating sheet: {name}")
        translated_sheets[name] = translate_dataframe(df, TARGET_LANGUAGE)

    # Generate output file name
    input_filename = os.path.basename(INPUT_FILE)
    output_filename = f"output/translated_{TARGET_LANGUAGE}_" + input_filename

    print("Writing translated Excel file...")
    write_excel_sheets(translated_sheets, output_filename)
    print(f"Translation complete. Output saved to {output_filename}")

if __name__ == "__main__":
    main()
