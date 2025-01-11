import pandas as pd
import csv
from typing import Dict, List, Optional
import os

class ICDMapper:
    def __init__(self):
        self.mappings: Dict[str, List[Dict]] = {}
        
    def read_mapping_file(self, file_path: str) -> None:
        """Read and process an ICD mapping file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            header = next(file)
            reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
            
            for row in reader:
                if len(row) >= 8:
                    counter = row[0].strip()
                    icd10_code = row[1].strip(' "')
                    who_update = row[2].strip()
                    icd10_descriptor = row[3].strip(' "')
                    icd10am_code = row[4].strip(' "')
                    aus_update = row[5].strip()
                    additive_map = row[6].strip(' "')
                    icd10am_descriptor = row[7].strip(' "')
                    
                    if icd10_code not in self.mappings:
                        self.mappings[icd10_code] = []
                        
                    mapping_entry = {
                        'counter': counter,
                        'icd10am_code': icd10am_code,
                        'icd10_descriptor': icd10_descriptor,
                        'icd10am_descriptor': icd10am_descriptor,
                        'who_update': who_update if who_update else None,
                        'aus_update': aus_update if aus_update else None,
                        'additive_map': additive_map if additive_map else None
                    }
                    
                    self.mappings[icd10_code].append(mapping_entry)
    
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
    
    def get_mapping(self, icd10_code: str) -> Optional[List[Dict]]:
        """Get all ICD-10-AM mappings for a given ICD-10 code."""
        return self.mappings.get(icd10_code)
    
    def generate_mapping_report(self, output_file: str) -> None:
        """Generate a detailed report of all mappings."""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("ICD-10 to ICD-10-AM Mapping Report\n")
            f.write("=" * 50 + "\n\n")
            
            for icd10_code, mappings in sorted(self.mappings.items()):
                f.write(f"ICD-10 Code: {icd10_code}\n")
                f.write(f"Description: {mappings[0]['icd10_descriptor']}\n")
                f.write("\nMapped ICD-10-AM Codes:\n")
                
                for mapping in mappings:
                    f.write(f"- {mapping['icd10am_code']}: {mapping['icd10am_descriptor']}\n")
                    if mapping['additive_map']:
                        f.write(f"  Additive Map: {mapping['additive_map']}\n")
                
                f.write("\n" + "-" * 50 + "\n\n")
    
    def export_to_excel(self, output_file: str) -> None:
        """Export all mappings to an Excel file."""
        rows = []
        for icd10_code, mappings in self.mappings.items():
            for mapping in mappings:
                rows.append({
                    'ICD-10 Code': icd10_code,
                    'ICD-10 Descriptor': mapping['icd10_descriptor'],
                    'ICD-10-AM Code': mapping['icd10am_code'],
                    'ICD-10-AM Descriptor': mapping['icd10am_descriptor'],
                    'WHO Update': mapping['who_update'],
                    'AUS Update': mapping['aus_update'],
                    'Additive Map': mapping['additive_map']
                })
        
        df = pd.DataFrame(rows)
        df.to_excel(output_file, index=False)

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
    
    # Generate reports
    mapper.generate_mapping_report(os.path.join(output_dir, 'icd_mapping_report.txt'))
    mapper.export_to_excel(os.path.join(output_dir, 'icd_mapping_report.xlsx'))
    
    print("\nProcessing complete! Check the output directory for results.")

if __name__ == "__main__":
    main()