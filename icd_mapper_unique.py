import pandas as pd
import csv
from typing import Dict, List, Optional
import os

class ICDMapper:
    def __init__(self):
        self.unique_icd10am_codes = set()
        self.code_descriptors = {}
        
    def read_mapping_file(self, file_path: str) -> None:
        """Read and process an ICD mapping file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            header = next(file)
            reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
            
            for row in reader:
                if len(row) >= 8:
                    icd10am_code = row[4].strip(' "')
                    icd10am_descriptor = row[7].strip(' "')
                    
                    if icd10am_code:  # Only process if there's a valid code
                        self.unique_icd10am_codes.add(icd10am_code)
                        # Store the descriptor (will overwrite if duplicate, which is fine)
                        self.code_descriptors[icd10am_code] = icd10am_descriptor
    
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
    
    def export_unique_codes(self, output_file: str) -> None:
        """Export unique ICD-10-AM codes to an Excel file."""
        rows = []
        for code in sorted(self.unique_icd10am_codes):
            rows.append({
                'ICD-10-AM Code': code,
                'Descriptor': self.code_descriptors[code]
            })
        
        df = pd.DataFrame(rows)
        df.to_excel(output_file, index=False)
        print(f"Found {len(rows)} unique ICD-10-AM codes")

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
    
    # Export unique codes
    mapper.export_unique_codes(os.path.join(output_dir, 'unique_icd10am_codes.xlsx'))
    
    print("\nProcessing complete! Check the output directory for results.")

if __name__ == "__main__":
    main()
