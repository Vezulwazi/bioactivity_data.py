# bioactivity_data.py
# Biological Activity Data Download and Processing

## Description
This Python script automates the download and processing of biological activity data from the USDA Phytochemical Database. The data is saved as CSV files and can be processed for further analysis. This tool is useful for researchers and analysts interested in exploring biological activities related to phytochemicals.

## Features
- Downloads CSV files containing biological activity data from the USDA database
- Processes and stores downloaded CSV files into a separate folder (`SDFS`)
- Handles missing or empty files gracefully
- Can be customized to analyze and process the data further

## Requirements
- Python 3.x
- `requests`
- `pubchempy`
- `pandas`

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/bioactivity_data.git
    cd bioactivity_data
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python bioactivity_data.py
    ```

4. The script will download the CSV files into the `bioact` folder and save the processed files in the `SDFS` folder.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
