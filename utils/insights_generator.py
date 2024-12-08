"""
Insights generation module for Report Insights App.
Handles calculation of metrics and generation of visualizations.
"""
import pandas as pd
import numpy as np
from numpy.typing import NDArray
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Tuple, Union, cast, Optional
import logging

logger = logging.getLogger(__name__)

class InsightsGenerator:
    """Handles generation of insights from processed data."""
    
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the InsightsGenerator.
        
        Args:
            df: Processed dataframe with standardized column names
        """
        self.df: pd.DataFrame = df
        
    def calculate_activity_conversions(self) -> pd.Series:
        """Calculate total conversions per activity."""
        try:
            # Explicitly cast the result to pd.Series to satisfy type checker
            conversions = cast(pd.Series, self.df.groupby('activity')['total_conversions'].sum())
            return cast(pd.Series, conversions.sort_values(ascending=False))
        except Exception as e:
            logger.error(f"Error calculating activity conversions: {e}")
            raise
            
    def get_top_activities(self, n: int = 10) -> pd.Series:
        """Get top N activities by conversion count."""
        try:
            return cast(pd.Series, self.calculate_activity_conversions().head(n))
        except Exception as e:
            logger.error(f"Error getting top activities: {e}")
            raise
            
    def calculate_summary_stats(self) -> Dict[str, float]:
        """Calculate basic summary statistics for conversions."""
        try:
            # Calculate total conversions directly from the dataframe
            total_conversions = int(self.df['total_conversions'].sum())
            
            # Calculate per-activity statistics
            activity_conversions = cast(pd.Series, self.calculate_activity_conversions())
            
            stats = {
                'Total Conversions': total_conversions,  # Total across all activities
                'Mean Conversions per Activity': float(activity_conversions.mean()),
                'Median Conversions per Activity': float(activity_conversions.median()),
                'Max Conversions per Activity': int(activity_conversions.max()),
                'Min Conversions per Activity': int(activity_conversions.min())
            }
            return stats
        except Exception as e:
            logger.error(f"Error calculating summary stats: {e}")
            raise
            
    def create_conversions_bar_chart(self, top_n: int = 10) -> go.Figure:
        """Create bar chart of conversions by activity."""
        try:
            top_activities = cast(pd.Series, self.get_top_activities(top_n))
            data = pd.DataFrame({
                'Activity': top_activities.index,
                'Conversions': top_activities.values
            })
            
            fig = px.bar(
                data,
                x='Activity',
                y='Conversions',
                title=f'Top {top_n} Activities by Conversions'
            )
            fig.update_layout(showlegend=False)
            return fig
        except Exception as e:
            logger.error(f"Error creating bar chart: {e}")
            raise
            
    def get_unique_activities(self) -> List[str]:
        """Get list of unique activities for filtering."""
        return sorted(cast(NDArray[np.str_], self.df['activity'].unique()).tolist())
        
    def get_unique_urls(self) -> List[str]:
        """Get list of unique URLs for filtering."""
        return sorted(cast(NDArray[np.str_], self.df['pageURL'].unique()).tolist())
        
    def create_conversions_time_series(
        self,
        selected_activities: Optional[List[str]] = None,
        selected_urls: Optional[List[str]] = None
    ) -> go.Figure:
        """
        Create line chart of conversions over time with optional filtering.
        
        Args:
            selected_activities: List of activities to include (None for all)
            selected_urls: List of URLs to include (None for all)
        """
        try:
            # Start with the full dataset
            df_filtered: pd.DataFrame = self.df.copy()
            
            # Apply activity filter if specified
            if selected_activities:
                mask = cast(pd.Series, df_filtered['activity'].isin(selected_activities))
                df_filtered = cast(pd.DataFrame, df_filtered.loc[mask])
                
            # Apply URL filter if specified
            if selected_urls:
                mask = cast(pd.Series, df_filtered['pageURL'].isin(selected_urls))
                df_filtered = cast(pd.DataFrame, df_filtered.loc[mask])
            
            # Group by date and calculate daily conversions
            grouped = df_filtered.groupby(['date', 'activity'])['total_conversions'].sum()
            daily_conversions = cast(pd.DataFrame, grouped.reset_index())
            
            # Create the line chart with a line for each activity
            fig = px.line(
                daily_conversions,
                x='date',
                y='total_conversions',
                color='activity',  # Create separate lines by activity
                title='Conversions Over Time',
                labels={
                    'date': 'Date',
                    'total_conversions': 'Total Conversions',
                    'activity': 'Activity'
                }
            )
            
            # Update layout for better readability
            fig.update_layout(
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=1.02
                ),
                margin=dict(r=150)  # Add right margin for legend
            )
            
            return fig
        except Exception as e:
            logger.error(f"Error creating time series chart: {e}")
            raise
            
    def export_insights(self) -> Dict[str, pd.DataFrame]:
        """Export basic insights as DataFrames."""
        try:
            activity_conversions = cast(pd.Series, self.calculate_activity_conversions())
            return {
                'activity_conversions': activity_conversions.reset_index().rename(
                    columns={'activity': 'Activity', 'total_conversions': 'Total Conversions'}
                ),
                'top_activities': cast(pd.Series, self.get_top_activities()).reset_index().rename(
                    columns={'activity': 'Activity', 'total_conversions': 'Total Conversions'}
                ),
                'daily_conversions': self.df.groupby('date')['total_conversions'].sum().reset_index().rename(
                    columns={'date': 'Date', 'total_conversions': 'Total Conversions'}
                )
            }
        except Exception as e:
            logger.error(f"Error exporting insights: {e}")
            raise
