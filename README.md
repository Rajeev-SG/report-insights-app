# Report Insights App

This project is a Streamlit application for analyzing tabular data from CSV and Excel files. The app provides data processing, validation, and insights generation capabilities.

## Features
- File Upload Support:
  - CSV files (.csv)
  - Excel files (.xlsx, .xls)
  - Automatic table detection within files
  - Support for various column name formats
- Data Processing:
  - Schema validation
  - Data type conversion
  - Missing value handling
  - Progress indicators for processing steps
- Data Preview:
  - View first 5 rows of processed data
  - Display total row and column counts
  - Show column data types and null counts
  - Show file metadata (name, size, type)
- Insights Generation:
  - Calculate total conversions per activity
  - Identify top performing activities
  - Generate summary statistics
  - Interactive visualizations
    - Bar chart of top activities
    - Filterable time series chart by activity and URL
- Data Export:
  - Export activity-wise conversions
  - Export daily conversion trends
  - Export top performing activities
- Error Handling:
  - Robust file format validation
  - Graceful handling of processing errors
  - User-friendly error messages
  - Comprehensive logging

## Project Structure
```
report-insights-app/
├── app.py                 # Main Streamlit application
├── utils/
│   ├── __init__.py       # Utils package initialization
│   ├── data_processor.py # Data processing utilities
│   └── insights_generator.py # Insights generation utilities
├── docs/
│   ├── streamlit-docs/   # Streamlit documentation
│   ├── notes.md          # Development notes
│   └── development_prompts.md
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
├── CHANGELOG.md         # Version history
└── BUGS.md             # Known issues
```

## Getting Started

### Prerequisites
- Python 3.7 or higher - https://www.python.org/downloads/
- Required packages (installed via requirements.txt):
  - streamlit==1.29.0
  - pandas>=2.2.0
  - numpy>=1.26.0
  - plotly>=5.24.1
  - openpyxl>=3.1.2
  - xlrd>=2.0.1
  - pyxlsb>=1.0.10

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd report-insights-app
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
To run the app, use the following command:
```bash
python -m streamlit run app.py
```

## Usage
1. Launch the app using the command above
2. Upload your CSV or Excel file using the file uploader
3. The app will automatically:
   - Detect the table location in your file
   - Standardize column names
   - Validate the data schema
   - Process and clean the data
4. View the processed data preview and statistics
5. Explore insights and visualizations:
   - View summary statistics
   - Analyze top performing activities
   - Explore conversion trends over time
   - Filter time series by activity and URL
6. Export insights as CSV files

## Development
- Follow the development guidelines in the documentation
- Use the utils package for data processing functionality
- Maintain consistent error handling and logging
- Update documentation for new features

## Contributing
Please read our contributing guidelines before submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
