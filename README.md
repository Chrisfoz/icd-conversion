# ICD Code Conversion Tool

A Python-based tool for converting and mapping ICD-10 codes to ICD-10-AM codes.

## Overview

This tool processes ICD code mapping files and provides functionality to:
- Convert ICD-10 codes to their ICD-10-AM equivalents
- Generate detailed mapping reports
- Export mappings to Excel format
- Handle complex one-to-many code relationships
- Extract unique ICD-10-AM codes
- Generate comprehensive code listings
- Convert Excel outputs to formatted text files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Chrisfoz/icd-conversion.git
cd icd-conversion
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows use:
venv\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Available Scripts

### 1. icd_mapper.py
The main script that provides comprehensive mapping functionality:
- Processes all mapping files in the data directory
- Generates detailed mapping reports
- Creates both text and Excel output files
- Handles one-to-many relationships between codes

```bash
python icd_mapper.py
```

### 2. icd_mapper_unique.py
Extracts and exports unique ICD-10-AM codes:
- Removes duplicate entries
- Maintains code-descriptor relationships
- Exports to Excel format

```bash
python icd_mapper_unique.py
```

### 3. icd_mapper_list.py
Generates a complete list of all ICD-10-AM codes:
- Includes duplicate entries (useful for frequency analysis)
- Handles multiple file encodings (utf-8, latin1, cp1252)
- Sorts codes for better readability

```bash
python icd_mapper_list.py
```

### 4. excel_to_txt.py
Converts Excel outputs to formatted text files:
- Creates structured text output with headers
- Includes category and code range documentation
- Uses tab-separated format for easy parsing

```bash
python excel_to_txt.py
```

## Output Files

The tool generates several output files in the `output` directory:

### From icd_mapper.py:
- `icd_mapping_report.txt`: Detailed text report of all mappings
- `icd_mapping_report.xlsx`: Complete mapping data in Excel format

### From icd_mapper_unique.py:
- `unique_icd10am_codes.xlsx`: List of unique ICD-10-AM codes with descriptors

### From icd_mapper_list.py:
- `icd10am_codes_all.xlsx`: Complete list of all ICD-10-AM codes (including duplicates)

### From excel_to_txt.py:
- `icd10am_codes.txt`: Formatted text version of the code listings

## Directory Structure

```
icd-conversion/
├── data/                # Place your ICD mapping files here
│   ├── ICD-10 to ICD-10-AM 11th Ed maps A00-V99.txt
│   ├── ICD-10 to ICD-10-AM 11th Ed maps Activity=.txt
│   ├── ICD-10 to ICD-10-AM 11th Ed maps W00-X29.txt
│   ├── ICD-10 to ICD-10-AM 11th Ed maps X30-X99.txt
│   └── ICD-10 to ICD-10-AM 11th Ed maps Y00-Z99.txt
├── output/             # Generated reports and files
├── icd_mapper.py       # Main mapping script
├── icd_mapper_unique.py # Unique codes extractor
├── icd_mapper_list.py  # Complete code listing generator
├── excel_to_txt.py     # Excel to text converter
├── requirements.txt
└── README.md
```

## Input File Format

The tool processes two types of mapping files:

### ICD Code Mapping Files
Files containing the main ICD-10 to ICD-10-AM code mappings with the following columns:
1. Counter
2. ICD-10 code
3. WHO update (1=Add, 2=Del)
4. ICD-10 code descriptor
5. ICD-10-AM Map
6. Aust update (1=Add, 2=Del)
7. Additive Map (+)
8. ICD-10-AM code descriptor

### Activity Category Mappings
The tool includes activity category mappings that classify different types of activities:
- Act=0: Sports activities (includes detailed subcategories for various sports like football, swimming, cycling, etc.)
- Act=1: Leisure activities
- Act=2: Working for income (includes specific industry codes like agriculture, mining, manufacturing, etc.)
- Act=3: Other types of work
- Act=4: Vital activities (resting, sleeping, eating)
- Act=8: Other specified activities
- Act=9: Unspecified activities

These activity categories are used to provide additional context and classification for the ICD codes, particularly for injury-related codes.

## Code Ranges

The tool handles different ranges of ICD codes:
- A00-V99: Various medical conditions
- W00-X29: External causes
- X30-X99: Environmental and accidental causes
- Y00-Z99: External causes and factors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
