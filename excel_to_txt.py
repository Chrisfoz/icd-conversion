import pandas as pd

def convert_excel_to_txt():
    # Read the Excel file
    df = pd.read_excel('output/icd10am_codes_all.xlsx')
    
    with open('output/icd10am_codes.txt', 'w', encoding='utf-8') as f:
        # Write header information
        f.write("# ICD-10-AM Code Categories\n")
        f.write("# Format: Each line contains tab-separated values\n")
        f.write("# Fields: ICD-10-AM_Code\tICD-10-AM_Descriptor\n")
        f.write("#\n")
        f.write("# Activity Categories:\n")
        f.write("# Act=0: Sports activities\n")
        f.write("# Act=1: Leisure activities\n")
        f.write("# Act=2: Working for income\n")
        f.write("# Act=3: Other types of work\n")
        f.write("# Act=4: Vital activities (resting, sleeping, eating)\n")
        f.write("# Act=8: Other specified activities\n")
        f.write("# Act=9: Unspecified activities\n")
        f.write("#\n")
        f.write("# Code Ranges:\n")
        f.write("# A00-V99: Various medical conditions\n")
        f.write("# W00-X29: External causes\n")
        f.write("# X30-X99: Environmental and accidental causes\n")
        f.write("# Y00-Z99: External causes and factors\n")
        f.write("#\n")
        f.write("# BEGIN DATA\n")
        
        # Write only ICD-10-AM Code and Descriptor
        for _, row in df.iterrows():
            f.write(f"{row['ICD-10-AM Code']}\t{row['ICD-10-AM Descriptor']}\n")

if __name__ == "__main__":
    convert_excel_to_txt()
    print("Conversion complete! Check output/icd10am_codes.txt")
