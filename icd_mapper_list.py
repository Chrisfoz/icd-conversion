import pandas as pd
import csv
from typing import Dict, List
import os

class ICDMapper:
    def __init__(self):
        self.icd10am_codes = []  # List instead of set to keep duplicates
        
    def read_mapping_file(self, file_path: str) -> None:
        """Read and process an ICD mapping file."""
        # Try different encodings
        encodings = ['utf-8', 'latin1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    header = next(file)
                    reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                    
                    for row in reader:
                        if len(row) >= 8:
                            icd10am_code = row[4].strip(' "')
                            icd10am_descriptor = row[7].strip(' "')
                            
                            if icd10am_code:  # Only process if there's a valid code
                                self.icd10am_codes.append({
                                    'ICD-10-AM Code': icd10am_code,
                                    'ICD-10-AM Descriptor': icd10am_descriptor
                                })
                # If we successfully read the file, break the loop
                break
            except UnicodeDecodeError:
                if encoding == encodings[-1]:  # If this was the last encoding to try
                    raise  # Re-raise the exception
                continue  # Try the next encoding
    
    def process_directory(self, directory_path: str) -> None:
        """Process all mapping files in a directory."""
        for filename in os.listdir(directory_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory_path, filename)
                try:
                    self.read_mapping_file(file_path)
                    print(f"Successfully processed {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
    
    def export_codes(self, output_file: str) -> None:
        """Export all ICD-10-AM codes to an Excel file."""
        df = pd.DataFrame(self.icd10am_codes)
        # Sort by ICD-10-AM Code for better readability
        df = df.sort_values('ICD-10-AM Code')
        df.to_excel(output_file, index=False)
        print(f"Exported {len(self.icd10am_codes)} ICD-10-AM code mappings")

def main():
    # Create mapper instance
    mapper = ICDMapper()
    
    # Set up directory paths
    directory_path = os.path.join(os.path.dirname(__file__), 'data')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process mapping files
    mapper.process_directory(directory_path)
    
    # Export codes
    mapper.export_codes(os.path.join(output_dir, 'icd10am_codes_all.xlsx'))
    
    print("\nProcessing complete! Check the output directory for results.")

if __name__ == "__main__":
    main()
