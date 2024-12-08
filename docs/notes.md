documentation process

1. find docs site
2. crawl one level with fire crawl
3. download docs as needed

single doc process

1. find docs site
2. scrape with jina.ai

cascade process
1. intial prompt
2. test
3. fix errors
4. document

initial prompt
I have a plan for a streamlit app here: @plan.md I have already built out the project scaffolding described here: @README.md , now based on the plan within plan.md can you write out a series of prompts that will be used to instruct Cascade to build each part of the app within the aforementioned plan. Write all of the prompts to a new markdown file. Each prompt should if neccessary include:

        Feature implementation details,
        Error handling and logging specifics,
        Documentation of ALL errors and fixes in CHANGELOG.md,
        The updating of BUGS.md with all issues and warnings,
        Verification all directories and files exist,
        The updating of README.md to reflect current project state including successfully implemented features,
        Testing procedures,
        Project Context: (e.g.'You are assisting with development on {project_name}, a {project_description}. Before proceeding, analyze the following documentation to understand the project: README Location: {readme_path} CHANGELOG Location: {changelog_path} BUGS Location: {bugs_path},
        Development Guidelines: Code Preservation, Maintain existing UI layout and styling exactly as is, Do not modify working code unless specifically required, Preserve all existing functionality, Keep current component structure intact
        Feature Implementation: Add only features explicitly requested, Implement changes incrementally, one at a time

first dev prompt
You are assisting with development on the Report Insights App, a Streamlit-based application for analyzing ad server reports and surfacing key insights. Before proceeding, analyze the following documentation:

README Location: @README.md 
CHANGELOG Location: @CHANGELOG.md 
BUGS Location: @BUGS.md
Streamlit Docs Location: @docs/streamlit-docs 

## Development Guidelines
- Code Preservation: Maintain existing functionality
- UI Consistency: Maintain existing UI layout and styling
- Incremental Development: Implement one feature at a time
- Include error handling/logging
- Documentation: Update all relevant documentation files
- Testing: Include appropriate test procedures

Implement the basic file upload functionality for the Report Insights App:
1. Create a file uploader component that accepts XLSX and CSV files
2. Add file format validation with user-friendly error messages
3. Implement basic data preview functionality

Requirements:
- Use st.file_uploader with appropriate file type restrictions
- Display uploaded file details (name, size, type)
- Show first 5 rows of data in a table format
- Handle and display appropriate error messages for invalid files


Testing:
- Test with valid XLSX and CSV files
- Test with invalid file formats
- Verify error message display

---

Well done, good work. Now: - Update README.md with new functionality and project file structure
- Document any issues in BUGS.md
- Update CHANGELOG.md with new features

---

2nd prompts


You are assisting with development on the Report Insights App, a Streamlit-based application for analyzing ad server reports and surfacing key insights. Before proceeding, analyze the following documentation:

README Location: @README.md  CHANGELOG Location: @CHANGELOG.md  BUGS Location: @BUGS.md  Streamlit Docs Location: @docs/streamlit-docs 

Development Guidelines
Code Preservation: Maintain existing functionality
UI Consistency: Maintain existing UI layout and styling
Incremental Development: Implement one feature at a time
Include error handling/logging
Documentation: Update all relevant documentation files
Testing: Include appropriate test procedures

Implement data processing functionality for uploaded files:
1. Create data processing utilities
2. Implement schema validation
3. Add data cleaning functions
4. Create data transformation pipeline

Requirements:
- Validate against example schema (table may begin several rows down):
  - activity (string)
  - activity_id (integer)
  - date (datetime64)
  - pageURL (string)
  - total_conversions (integer)
- Handle missing values
- Convert data types appropriately
- Implement data cleaning functions
- Add progress indicators for processing steps


Testing:
- Test with various data formats
- Verify data type conversions
- Test missing value handling
- Validate error logging

Well done, good work. Now: - Update README.md with new functionality and project file structure
- Document any issues in BUGS.md
- Update CHANGELOG.md with new features

3rd prompt

You are assisting with development on the Report Insights App, a Streamlit-based application for analyzing ad server reports and surfacing key insights. Before proceeding, analyze the following documentation:

README Location: @README.md  CHANGELOG Location: @CHANGELOG.md  BUGS Location: @BUGS.md  Streamlit Docs Location: @docs/streamlit-docs 

Development Guidelines
Code Preservation: Maintain existing functionality
UI Consistency: Maintain existing UI layout and styling
Incremental Development: Implement one feature at a time
Include error handling/logging
Documentation: Update all relevant documentation files
Testing: Include appropriate test procedures

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

Testing:
- Verify calculations accuracy
- Test visualization rendering
- Validate export functionality