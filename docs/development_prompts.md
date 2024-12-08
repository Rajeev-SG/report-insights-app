# Development Prompts for Report Insights App

This document contains a series of prompts designed to guide the development of the Report Insights Streamlit application. Each prompt is structured to ensure comprehensive implementation of features while maintaining code quality and documentation.

## Project Context Template
```
You are assisting with development on the Report Insights App, a Streamlit-based application for analyzing ad server reports and surfacing key insights. Before proceeding, analyze the following documentation:

README Location: ./README.md
CHANGELOG Location: ./CHANGELOG.md
BUGS Location: ./BUGS.md
```

## Development Guidelines
- Code Preservation: Maintain existing functionality
- UI Consistency: Maintain existing UI layout and styling
- Incremental Development: Implement one feature at a time
- Documentation: Update all relevant documentation files
- Testing: Include appropriate test procedures

## Prompts

### 1. Basic App Structure and File Upload
```
Implement the basic file upload functionality for the Report Insights App:
1. Create a file uploader component that accepts XLSX and CSV files
2. Add file format validation with user-friendly error messages
3. Implement basic data preview functionality
4. Update documentation to reflect new features

Requirements:
- Use st.file_uploader with appropriate file type restrictions
- Display uploaded file details (name, size, type)
- Show first 5 rows of data in a table format
- Handle and display appropriate error messages for invalid files
- Update README.md with new functionality
- Document any issues in BUGS.md
- Update CHANGELOG.md with new features

Testing:
- Test with valid XLSX and CSV files
- Test with invalid file formats
- Verify error message display
```

### 2. Data Processing and Validation
```
Implement data processing functionality for uploaded files:
1. Create data processing utilities
2. Implement schema validation
3. Add data cleaning functions
4. Create data transformation pipeline

Requirements:
- Validate against example schema:
  - activity (string)
  - activity_id (integer)
  - date (datetime64)
  - pageURL (string)
  - total_conversions (integer)
- Handle missing values
- Convert data types appropriately
- Implement data cleaning functions
- Add progress indicators for processing steps
- Update documentation with new features
- Log all processing errors

Testing:
- Test with various data formats
- Verify data type conversions
- Test missing value handling
- Validate error logging
```

### 3. Basic Insights Generation
```
Implement basic insights generation functionality:
1. Calculate total conversions per activity
2. Identify top performing activities
3. Generate basic summary statistics
4. Create initial visualizations

Requirements:
- Calculate and display:
  - Total conversions by activity
  - Top 10 activities by conversion
  - Basic statistics (mean, median, max, min)
- Create initial visualizations:
  - Bar chart for conversions per activity
  - Line chart for conversions over time
- Add export functionality for basic insights
- Update documentation

Testing:
- Verify calculations accuracy
- Test visualization rendering
- Validate export functionality
```

### 4. Advanced Analytics Implementation
```
Implement advanced analytics features:
1. Add anomaly detection
2. Create correlation analysis
3. Implement trend analysis
4. Generate detailed insights

Requirements:
- Implement anomaly detection algorithm
- Create correlation heatmap
- Add trend analysis with seasonality
- Generate detailed statistical insights
- Update documentation with new analytics features
- Add error handling for complex calculations

Testing:
- Validate anomaly detection accuracy
- Test correlation calculations
- Verify trend analysis results
```

### 5. Interactive Visualization Enhancement
```
Enhance visualization capabilities:
1. Add interactive filters
2. Implement drill-down capabilities
3. Create dynamic chart updates
4. Add custom visualization options

Requirements:
- Add date range selector
- Implement activity and URL filters
- Create interactive charts with hover details
- Add visualization customization options
- Ensure responsive design
- Update documentation

Testing:
- Test filter functionality
- Verify chart interactivity
- Validate responsive design
- Test custom visualization options
```

### 6. Export and Reporting Features
```
Implement export and reporting functionality:
1. Add chart export options
2. Create PDF report generation
3. Implement data export features
4. Add batch processing capability

Requirements:
- Enable chart export (PNG, JPEG)
- Implement PDF report generation
- Add CSV/Excel export options
- Create batch processing for multiple files
- Update documentation with export features

Testing:
- Verify all export formats
- Test PDF generation
- Validate batch processing
- Check exported file integrity
```

### 7. Performance Optimization
```
Optimize app performance:
1. Implement data caching
2. Add async processing
3. Optimize memory usage
4. Enhance error handling

Requirements:
- Implement st.cache for data processing
- Add async loading indicators
- Optimize memory usage for large datasets
- Enhance error handling and messaging
- Update performance documentation
- Log performance metrics

Testing:
- Benchmark processing times
- Test memory usage
- Verify cache effectiveness
- Validate error handling
```

### 8. Final Polish and Documentation
```
Complete final polishing and documentation:
1. Conduct comprehensive testing
2. Update all documentation
3. Add user guide
4. Implement final UI improvements

Requirements:
- Complete end-to-end testing
- Update all documentation files
- Create comprehensive user guide
- Add final UI improvements
- Document known issues
- Create release notes

Testing:
- Full system testing
- Documentation review
- UI/UX testing
- Performance validation
```

## Note on Implementation
Each prompt should be implemented sequentially, ensuring that:
1. All changes are documented in CHANGELOG.md
2. Any issues are recorded in BUGS.md
3. README.md is kept up to date
4. Each feature is thoroughly tested before moving to the next
5. Code quality and consistency are maintained throughout
