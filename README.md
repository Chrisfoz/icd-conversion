# ICD Code Conversion Tool

A Python-based tool for converting and mapping ICD-10 codes to ICD-10-AM codes.

## Features

- Process multiple ICD code mapping files
- Convert ICD-10 codes to ICD-10-AM codes
- Generate detailed mapping reports
- Export mappings to Excel
- Handle complex mappings with multiple relationships

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Chrisfoz/icd-conversion.git
cd icd-conversion
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your ICD mapping files in the `data` directory
2. Run the conversion script:
```bash
python icd_mapper.py
```

3. Find the output in:
- `icd_mapping_report.txt` for detailed text report
- `icd_mapping_report.xlsx` for Excel spreadsheet

## Input File Format

The tool expects text files with the following columns:
- Counter
- ICD-10 code
- WHO update
- ICD-10 code descriptor
- ICD-10-AM Map
- Aust update
- Additive Map
- ICD-10-AM code descriptor

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.