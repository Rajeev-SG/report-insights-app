# Changelog

All notable changes to the Report Insights App will be documented in this file.

## [Unreleased]
- Initial setup of the Streamlit app.
- Created README, BUGS, and CHANGELOG files.

## [0.4.0] - 2024-12-08

### Added
- Insights Generation functionality
  - Implemented InsightsGenerator class for data analysis
  - Added calculation of total conversions per activity
  - Added identification of top performing activities
  - Added basic summary statistics (total, mean, median, max, min)
  - Added interactive visualizations:
    - Bar chart showing top activities by conversions
    - Time series chart with activity and URL filtering
  - Added data export functionality for insights
- Enhanced UI
  - Added filter controls for time series visualization
  - Added summary statistics display
  - Added download buttons for exporting insights

### Fixed
- Type checking issues in insights generation code
- Improved error handling in data processing

## [0.3.0] - 2024-12-07

### Added
- Data processing functionality
  - Implemented DataProcessor class for data validation and cleaning
  - Added schema validation for required columns
  - Added support for various column name formats
  - Implemented data type conversion and validation
  - Added missing value handling
- Automatic table detection
  - Added support for finding tables that don't start at row 1
  - Intelligent column name matching
- Enhanced data preview
  - Added column data type information
  - Added null value counts
  - Added data processing progress indicators
- Improved error handling
  - Added comprehensive logging
  - Enhanced error messages for data processing issues

### Changed
- Restructured project to include utils package
- Enhanced file reading to support tables at different positions
- Updated documentation with new features and project structure

## [0.2.1] - 2024-12-07
### Changed
- Improved error handling in file processing
- Added explicit initialization of dataframe variable
- Enhanced unsupported file format handling
- Added defensive programming checks

## [0.2.0] - 2024-12-07
### Added
- File upload functionality for CSV and Excel files
- Data preview feature showing first 5 rows
- File metadata display (name, size, type)
- Support for multiple Excel formats (.xlsx, .xls)
- Comprehensive error handling and validation
- Updated dependencies in requirements.txt

### Changed
- Enhanced UI with wide layout
- Improved error messages for better user experience

## [0.1.0] - 2023-02-20
- Initial project setup.
- Added initial changelog entries.
