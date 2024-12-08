"""
Data processing utilities for Report Insights App.
Handles data validation, cleaning, and transformation.
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles data processing operations for uploaded files."""
    
    EXPECTED_SCHEMA = {
        'activity': str,
        'activity_id': 'Int64',  # Using Int64 to handle nullable integers
        'date': 'datetime64[ns]',
        'pageURL': str,
        'total_conversions': 'Int64'
    }
    
    # Map of possible column names to standardized names
    COLUMN_NAME_MAPPING = {
        'activity': ['activity', 'Activity', 'ACTIVITY'],
        'activity_id': ['activity_id', 'Activity ID', 'Activity Id', 'ACTIVITY_ID', 'ActivityID'],
        'date': ['date', 'Date', 'DATE'],
        'pageURL': ['pageURL', 'PageURL', 'Page URL', 'PageURL (string)', 'page_url', 'PAGE_URL'],
        'total_conversions': ['total_conversions', 'Total Conversions', 'TotalConversions', 'TOTAL_CONVERSIONS']
    }
    
    def __init__(self):
        """Initialize the DataProcessor."""
        self.data = None
        self.validation_errors = []
        
    def standardize_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize column names to match expected schema.
        
        Args:
            df: Input dataframe
            
        Returns:
            pd.DataFrame: Dataframe with standardized column names
        """
        standardized_df = df.copy()
        current_columns = df.columns.str.strip()
        
        # Create reverse mapping for column standardization
        reverse_mapping = {}
        for standard_name, variations in self.COLUMN_NAME_MAPPING.items():
            for variant in variations:
                reverse_mapping[variant.lower()] = standard_name
        
        # Create new column mapping
        column_mapping = {}
        for col in current_columns:
            col_lower = col.lower()
            if col_lower in reverse_mapping:
                column_mapping[col] = reverse_mapping[col_lower]
        
        # Rename columns if mapping exists
        if column_mapping:
            standardized_df = standardized_df.rename(columns=column_mapping)
            logger.info(f"Standardized columns: {column_mapping}")
        
        return standardized_df
    
    def validate_schema(self, df: pd.DataFrame) -> bool:
        """
        Validate if the dataframe matches the expected schema.
        
        Args:
            df: Input dataframe to validate
            
        Returns:
            bool: True if schema is valid, False otherwise
        """
        try:
            required_columns = set(self.EXPECTED_SCHEMA.keys())
            actual_columns = set(df.columns)
            
            # Check for missing columns
            missing_columns = required_columns - actual_columns
            if missing_columns:
                self.validation_errors.append(f"Missing required columns: {missing_columns}")
                return False
                
            return True
            
        except Exception as e:
            logger.error(f"Schema validation error: {str(e)}")
            self.validation_errors.append(f"Schema validation error: {str(e)}")
            return False
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the input dataframe by handling missing values and data type conversions.
        
        Args:
            df: Input dataframe to clean
            
        Returns:
            pd.DataFrame: Cleaned dataframe
        """
        try:
            # Create a copy to avoid modifying the original
            cleaned_df = df.copy()
            
            # Handle missing values
            cleaned_df['activity'] = cleaned_df['activity'].fillna('Unknown')
            cleaned_df['pageURL'] = cleaned_df['pageURL'].fillna('')
            
            # Convert data types
            for column, dtype in self.EXPECTED_SCHEMA.items():
                if column in cleaned_df.columns:
                    try:
                        if dtype == 'datetime64[ns]':
                            cleaned_df[column] = pd.to_datetime(cleaned_df[column], errors='coerce')
                        else:
                            cleaned_df[column] = cleaned_df[column].astype(dtype)
                    except Exception as e:
                        logger.warning(f"Error converting {column} to {dtype}: {str(e)}")
            
            return cleaned_df
            
        except Exception as e:
            logger.error(f"Data cleaning error: {str(e)}")
            raise
    
    def process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Main data processing pipeline.
        
        Args:
            df: Input dataframe to process
            
        Returns:
            pd.DataFrame: Processed dataframe
        """
        try:
            logger.info("Starting data processing pipeline")
            
            # Standardize column names
            df = self.standardize_column_names(df)
            
            # Validate schema
            if not self.validate_schema(df):
                error_msg = "Schema validation failed: " + "; ".join(self.validation_errors)
                logger.error(error_msg)
                raise ValueError(error_msg)
            
            # Clean data
            logger.info("Cleaning data...")
            processed_df = self.clean_data(df)
            
            logger.info("Data processing completed successfully")
            return processed_df
            
        except Exception as e:
            logger.error(f"Data processing failed: {str(e)}")
            raise
    
    def get_validation_errors(self) -> List[str]:
        """Return list of validation errors."""
        return self.validation_errors
