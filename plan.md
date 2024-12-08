**Prompt for LLM-Assisted Coding Agent/IDE to Build the App:**

---

**Project Title:** Ad Server Report Insights Streamlit App

**Objective:**

Create a Python-based Streamlit application that allows users to upload ad server reports in XLSX or CSV format and automatically surfaces key insights from these reports. The app should provide data analysis and visualizations to help users understand conversions associated with activities, page URLs, dates, and more.

---

### **Application Overview:**

- **Input:** Ad server reports containing fields such as:
  - `activity`
  - `activity_id`
  - `date`
  - `pageURL`
  - **Metrics:** e.g., `total_conversions`

```
  example_schema = {  
    "activity": "string",  
    "activity_id": "integer",  
    "date": "datetime64",  
    "pageURL": "string",  
    "total_conversions": "integer"  
}  
```

- **Output:** Interactive insights and visualizations that highlight key metrics and trends within the data.

---

### **Core Functionality:**

1. **File Upload:**
   - Implement a file uploader that accepts XLSX and CSV files.
   - Validate the uploaded file format and provide error messages for unsupported formats.

2. **Data Processing:**
   - Read and parse the uploaded file using appropriate libraries (`pandas`, `openpyxl`, or `csv`).
   - Automatically identify the fields and metrics present in the report.
   - Handle missing values and data cleaning as necessary.

3. **Insight Generation:**
   - **Total Conversions per Activity:**
     - Calculate and display the total conversions attributed to each unique activity.
   - **Most Popular Page URLs per Activity:**
     - For each activity, list the top page URLs based on conversions or visits.
   - **Conversions Over Time:**
     - Analyze and visualize conversions by date to identify trends.
   - **Top Performing Activities:**
     - Identify activities with the highest conversions.
   - **Conversion Breakdown:**
     - Provide a breakdown of conversions by activity, page URL, and date.
   - **Anomaly Detection:**
     - Highlight any significant deviations or outliers in the data.
   - **Summary Statistics:**
     - Display mean, median, maximum, and minimum values for conversions and other metrics.

4. **Data Visualization:**
   - Use interactive charts and graphs to present insights:
     - **Bar Charts:** Conversions per activity, top page URLs.
     - **Line Charts:** Conversion trends over time.
     - **Pie Charts:** Distribution of conversions among activities or page URLs.
     - **Heatmaps:** Correlation between different metrics.
   - Allow users to interact with visualizations (e.g., hover for details, zoom, filter).

5. **User Interface (UX/UI):**
   - Design a clean and intuitive layout using Streamlit components.
   - **Navigation:**
     - Use tabs or sidebar navigation for different sections (e.g., Data Upload, Insights, Visualizations).
   - **Filters and Controls:**
     - Date range selector.
     - Activity and page URL filters.
     - Options to select specific metrics or fields for analysis.
   - **Data Preview:**
     - Display a preview of the uploaded data (first few rows) for confirmation.
   - **Responsive Design:**
     - Ensure the app is accessible on various devices and screen sizes.

6. **Export and Download Options:**
   - Provide options to download generated insights and visualizations:
     - Export charts as images (PNG, JPEG).
     - Download data tables as CSV or Excel files.
     - Generate a PDF report summarizing key insights.

7. **Performance Optimization:**
   - Optimize data processing for large datasets.
   - Implement asynchronous loading for improved responsiveness.

8. **Error Handling and Validation:**
   - Provide user-friendly error messages for issues like incorrect file format, missing data, or processing errors.
   - Validate user inputs and selections to prevent crashes.

9. **Extensibility:**
   - Write modular code with functions and classes for easy maintenance and future enhancements.
   - Allow for additional metrics and insights to be added with minimal changes.

---

### **Key Features and Insights:**

- **Automatic Field Recognition:**
  - The app should dynamically adjust to different report structures, identifying available fields and metrics.

- **Customizable Insights:**
  - Users can select which insights to generate based on available data.

- **Interactive Visualizations:**
  - Enable users to interact with charts for deeper exploration (e.g., click on a bar to filter data).

---

### **Key Python Libraries and Tools:**

- **Streamlit:** For building the web application interface.
- **OpenPyXL/XLRD/CSV:** For reading Excel and CSV files.
- **Pandas:** For data manipulation and analysis.
- **NumPy:** For numerical operations.
- **Datetime:** For date and time operations.

### **Optional/additional Python Libraries and Tools:**
- **Matplotlib/Seaborn/Plotly:** For creating static and interactive visualizations.
- **Altair:** For declarative statistical visualization.
- **Plotly Express:** For easy-to-use high-level interface to Plotly.

---

### **User Experience (UX) Plan:**

1. **Landing Page:**
   - Welcome message with brief instructions.
   - File upload section prominently displayed.

2. **Data Upload and Preview:**
   - After file upload, display a preview of the data.
   - Show detected fields and metrics.
   - Provide options to select or deselect fields for analysis.

3. **Insights Dashboard:**
   - **Summary Section:**
     - Display key metrics at a glance (e.g., total conversions, number of activities).
   - **Visualizations:**
     - Organized into tabs or sections (e.g., Activities Overview, Page URL Analysis, Time Trends).
   - **Filters Panel:**
     - Interactive controls for users to filter data and refine insights.
   - **Anomaly Alerts:**
     - Notifications or highlights for any detected anomalies or significant changes.

4. **Reports and Exporting:**
   - Options to download data, charts, and reports.
   - Customizable report generation based on user-selected insights.

5. **Help and Support:**
   - Provide tooltips or help icons explaining various features.
   - Include a contact or feedback option for user support.

---
### **Development Phases:**

1. MVP Phase (Core Features):  
   - File upload and basic validation  
   - Essential visualizations  
   - Basic insights  

2. Enhancement Phase:  
   - Advanced analytics  
   - Export functionality  
   - Performance optimization  

---

### **Additional Considerations:**

- **Data Security:**
  - Ensure agent is directed to write well commented code with proper error handling and logging

- **Documentation:**
  - Ensure agent includes instructions in each prompt to update the changelog, readme, and bugs files after each implementation

- **Logging and Monitoring:**
  - Implement logging to track usage patterns and identify potential issues.

- **Deployment:**
  - Provide instructions or scripts for deploying the app on a server or cloud platform (e.g., Heroku, AWS).

---

**Please provide the prompts to develop each section of the Streamlit application based on the specifications provided above.**