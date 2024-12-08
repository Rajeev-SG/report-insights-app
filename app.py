import streamlit as st
import pandas as pd
import io
from utils.data_processor import DataProcessor
from utils.insights_generator import InsightsGenerator
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="Report Insights App",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title('Report Insights App')
st.write('Upload your CSV or Excel files for analysis.')

# File uploader
uploaded_file = st.file_uploader(
    "Choose a file",
    type=['csv', 'xlsx', 'xls'],
    help="Upload a CSV or Excel file"
)

if uploaded_file is not None:
    # Display file details
    file_details = {
        "Filename": uploaded_file.name,
        "File size": f"{uploaded_file.size / 1024:.2f} KB",
        "File type": uploaded_file.type
    }
    
    st.write("### File Details")
    for key, value in file_details.items():
        st.write(f"**{key}:** {value}")
    
    try:
        df = None
        # Read the file based on its type
        if uploaded_file.name.endswith('.csv'):
            # Try different starting rows for CSV
            for skiprows in range(15):  # Try first 15 rows
                try:
                    temp_df = pd.read_csv(uploaded_file, skiprows=skiprows)
                    # Check if any of the expected column variations exist
                    if any(col.strip() in [var for vars in DataProcessor.COLUMN_NAME_MAPPING.values() for var in vars] 
                          for col in temp_df.columns):
                        df = temp_df
                        st.info(f"Found table data starting at row {skiprows + 1}")
                        break
                except Exception:
                    continue
                finally:
                    # Reset file pointer for next attempt
                    uploaded_file.seek(0)
        elif uploaded_file.name.endswith(('.xlsx', '.xls')):
            # Try different starting rows for Excel
            for skiprows in range(15):  # Try first 15 rows
                try:
                    temp_df = pd.read_excel(
                        uploaded_file,
                        skiprows=skiprows,
                        engine='openpyxl' if uploaded_file.name.endswith('.xlsx') else 'xlrd'
                    )
                    # Check if any of the expected column variations exist
                    if any(col.strip() in [var for vars in DataProcessor.COLUMN_NAME_MAPPING.values() for var in vars] 
                          for col in temp_df.columns):
                        df = temp_df
                        st.info(f"Found table data starting at row {skiprows + 1}")
                        break
                except Exception:
                    continue
                finally:
                    # Reset file pointer for next attempt
                    uploaded_file.seek(0)
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            st.stop()
        
        if df is None:
            st.error("Could not find valid table data in the first 15 rows of the file.")
            st.stop()
            
        # Only proceed if we successfully loaded the dataframe
        if df is not None:
            with st.spinner('Processing data...'):
                try:
                    # Process the data
                    processor = DataProcessor()
                    df = processor.standardize_column_names(df)
                    df = processor.process_data(df)
                    
                    # Generate insights
                    insights = InsightsGenerator(df)
                    
                    # Display data preview
                    st.write("### Data Preview")
                    st.dataframe(df.head())
                    
                    # Display summary statistics
                    st.write("### Summary Statistics")
                    stats = insights.calculate_summary_stats()
                    col1, col2 = st.columns(2)
                    for i, (metric, value) in enumerate(stats.items()):
                        if i % 2 == 0:
                            col1.metric(metric, value)
                        else:
                            col2.metric(metric, value)
                    
                    # Display visualizations
                    st.write("### Visualizations")
                    
                    # Bar chart of top activities
                    st.plotly_chart(
                        insights.create_conversions_bar_chart(),
                        use_container_width=True
                    )
                    
                    # Time series filters
                    st.write("### Conversions Over Time")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        activities = insights.get_unique_activities()
                        selected_activities = st.multiselect(
                            "Filter by Activities",
                            options=activities,
                            default=activities[:5] if len(activities) > 5 else activities,
                            help="Select one or more activities to display"
                        )
                    
                    with col2:
                        urls = insights.get_unique_urls()
                        selected_urls = st.multiselect(
                            "Filter by URLs",
                            options=urls,
                            help="Select one or more URLs to display"
                        )
                    
                    # Time series chart with filters
                    st.plotly_chart(
                        insights.create_conversions_time_series(
                            selected_activities=selected_activities,
                            selected_urls=selected_urls
                        ),
                        use_container_width=True
                    )
                    
                    # Export functionality
                    st.write("### Export Insights")
                    export_data = insights.export_insights()
                    
                    for name, df in export_data.items():
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label=f"Download {name.replace('_', ' ').title()}",
                            data=csv,
                            file_name=f"{name}.csv",
                            mime="text/csv"
                        )
                    
                except Exception as e:
                    st.error(f"Error processing data: {str(e)}")
                    st.stop()
        
    except Exception as e:
        st.error(f"Error reading the file: {str(e)}")
        st.write("Please make sure your file is properly formatted and try again.")
        if "No engine for filetype" in str(e):
            st.write("This error might be due to missing Excel dependencies. Please contact the administrator.")
