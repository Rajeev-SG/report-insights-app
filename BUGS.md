# Known Issues and Bugs

## Active Issues

### Data Processing
- [DP-1] Table detection may not work for files with multiple tables
- [DP-2] Column name standardization might not catch all possible variations
- [DP-3] Performance may degrade with very large files (>100MB)

### File Handling
- [FH-1] Excel binary files (.xlsb) support is untested
- [FH-2] File upload size limit needs to be configured

### User Interface
- [UI-1] Progress indicators could be more granular
- [UI-2] Error messages could be more descriptive for specific data type conversion failures

### Insights Generation
- [IG-1] Time series visualization may become cluttered with many activities
- [IG-2] URL filter dropdown may be difficult to use with many unique URLs
- [IG-3] Memory usage may be high when filtering large datasets

## Planned Improvements

### Data Processing
- Implement caching for processed data
- Add support for custom column name mappings
- Optimize performance for large files

### File Handling
- Add support for more file formats
- Implement file validation before processing
- Add batch processing capabilities

### User Interface
- Add detailed processing logs view
- Improve progress tracking granularity
- Enhance error message clarity

## Resolved Issues

### [0.3.0] - 2024-12-07
- Fixed issue with tables not being detected when not starting at row 1
- Fixed column name case sensitivity problems
- Improved error handling for data type conversions

### [0.2.1] - 2024-12-06
- Fixed file upload error handling
- Improved error messages for unsupported file types

### [0.4.0] - 2024-12-08
- Fixed type checking issues in insights generation code
- Improved error handling in data processing
- Fixed column name standardization issues
- Fixed data type conversion errors
