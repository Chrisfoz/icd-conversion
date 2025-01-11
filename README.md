# ICD Code Conversion Tool

A Python-based tool for converting and mapping ICD-10 codes to ICD-10-AM codes.

## Overview

This tool processes ICD code mapping files and provides functionality to:
- Convert ICD-10 codes to their ICD-10-AM equivalents
- Generate detailed mapping reports
- Export mappings to Excel format
- Handle complex one-to-many code relationships

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Chrisfoz/icd-conversion.git
cd icd-conversion
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your ICD mapping files in the `data` directory
2. Run the script:
```bash
python icd_mapper.py
```

The tool will process all .txt files in the data directory and generate:
- A detailed text report (`output/icd_mapping_report.txt`)
- An Excel spreadsheet (`output/icd_mapping_report.xlsx`)

## Directory Structure

```
icd-conversion/
├── data/           # Place your ICD mapping files here
├── output/         # Generated reports will be saved here
├── icd_mapper.py   # Main script
├── requirements.txt
└── README.md
```

## Input File Format

The tool expects text files with comma-separated values and the following columns:
1. Counter
2. ICD-10 code
3. WHO update (1=Add, 2=Del)
4. ICD-10 code descriptor
5. ICD-10-AM Map
6. Aust update (1=Add, 2=Del)
7. Additive Map (+)
8. ICD-10-AM code descriptor

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.