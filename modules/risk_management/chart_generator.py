"""
Risk Management Chart Generator
Generates visualizations for risk data
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, Optional
import numpy as np


class RiskChartGenerator:
    """Generates charts for risk management data"""
    
    def __init__(self, data: pd.DataFrame, output_folder: str, config: Dict, logger=None):
        """
        Initialize the chart generator
        
        Args:
            data: Consolidated risk data
            output_folder: Path to save generated charts
            config: Chart configuration
            logger: Logger instance
        """
        self.data = data
        self.output_folder = Path(output_folder)
        self.config = config
        self.logger = logger
        
        # Create output folder if it doesn't exist
        self.output_folder.mkdir(parents=True, exist_ok=True)
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.facecolor'] = 'white'
    
    def _log(self, message, level="info"):
        """Log message if logger is available"""
        if self.logger:
            getattr(self.logger, level)(message)
        else:
            print(f"{level.upper()}: {message}")
    
    def generate_all_charts(self) -> Dict[str, str]:
        """
        Generate all risk management charts
        
        Returns:
            Dictionary mapping chart names to file paths
        """
        self._log("Generating risk management charts...")
        
        chart_files = {}
        
        try:
            # 1. Stacked bar chart: Open risks priorities per business area
            stacked_bar_path = self.generate_stacked_bar_chart()
            if stacked_bar_path:
                chart_files['stacked_bar'] = stacked_bar_path
            
            # 2. Pie chart: Operational Risk Statuses
            pie_status_path = self.generate_status_pie_chart()
            if pie_status_path:
                chart_files['pie_status'] = pie_status_path
            
            # 3. Pie chart: % Split Open Risk Categories
            pie_categories_path = self.generate_categories_pie_chart()
            if pie_categories_path:
                chart_files['pie_categories'] = pie_categories_path
            
            self._log(f"Generated {len(chart_files)} charts successfully")
            
        except Exception as e:
            self._log(f"Error generating charts: {str(e)}", "error")
        
        return chart_files
    
    def generate_stacked_bar_chart(self) -> Optional[str]:
        """
        Generate stacked bar chart: Open risks priorities per business area
        
        Returns:
            Path to saved chart
        """
        try:
            self._log("Creating stacked bar chart: Open Risks Priorities per Business Area")
            
            # Filter for open risks only
            open_risks = self.data[self.data['Status'] == 'Open'].copy()
            
            if open_risks.empty:
                self._log("No open risks found for stacked bar chart", "warning")
                return None
            
            # Create pivot table: Business Area x Risk Rating
            pivot_data = pd.crosstab(
                open_risks['Business Area'],
                open_risks['Risk Rating']
            )
            
            # Ensure priority order (High, Medium, Low)
            priority_order = ['High', 'Medium', 'Low']
            existing_priorities = [p for p in priority_order if p in pivot_data.columns]
            pivot_data = pivot_data[existing_priorities]
            
            # Create stacked bar chart
            fig, ax = plt.subplots(
                figsize=(
                    self.config.get('stacked_bar', {}).get('width', 10),
                    self.config.get('stacked_bar', {}).get('height', 6)
                )
            )
            
            # Define colors for priorities
            colors = {'High': '#d32f2f', 'Medium': '#ff9800', 'Low': '#4caf50'}
            colors_list = [colors.get(p, '#808080') for p in existing_priorities]
            
            pivot_data.plot(
                kind='bar',
                stacked=True,
                ax=ax,
                color=colors_list,
                width=0.7
            )
            
            # Formatting
            ax.set_title(
                self.config.get('stacked_bar', {}).get('title', 'Open Risks Priorities per Business Area'),
                fontsize=14,
                fontweight='bold',
                pad=20
            )
            ax.set_xlabel('Business Area', fontsize=12, fontweight='bold')
            ax.set_ylabel('Number of Open Risks', fontsize=12, fontweight='bold')
            ax.legend(title='Priority', loc='upper right', framealpha=0.9)
            
            # Rotate x-axis labels for readability
            plt.xticks(rotation=45, ha='right')
            
            # Add value labels on bars
            for container in ax.containers:
                ax.bar_label(container, label_type='center', fontsize=9)
            
            plt.tight_layout()
            
            # Save chart
            filename = self.config.get('stacked_bar', {}).get('filename', 'risk_priorities_stacked_bar.png')
            filepath = self.output_folder / filename
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            plt.close()
            
            self._log(f"  Saved: {filepath}")
            return str(filepath)
            
        except Exception as e:
            self._log(f"Error creating stacked bar chart: {str(e)}", "error")
            return None
    
    def generate_status_pie_chart(self) -> Optional[str]:
        """
        Generate pie chart: Operational Risk Statuses
        
        Returns:
            Path to saved chart
        """
        try:
            self._log("Creating pie chart: Operational Risk Statuses")
            
            # Count risks by status
            status_counts = self.data['Status'].value_counts()
            
            if status_counts.empty:
                self._log("No status data found for pie chart", "warning")
                return None
            
            # Create pie chart
            fig, ax = plt.subplots(
                figsize=(
                    self.config.get('pie_status', {}).get('width', 8),
                    self.config.get('pie_status', {}).get('height', 6)
                )
            )
            
            # Define colors
            colors = {'Open': '#ff6b6b', 'Closed': '#51cf66'}
            pie_colors = [colors.get(status, '#808080') for status in status_counts.index]
            
            wedges, texts, autotexts = ax.pie(
                status_counts.values,
                labels=status_counts.index,
                autopct='%1.1f%%',
                startangle=90,
                colors=pie_colors,
                explode=[0.05] * len(status_counts)  # Slight separation
            )
            
            # Formatting
            ax.set_title(
                self.config.get('pie_status', {}).get('title', 'Operational Risk Statuses'),
                fontsize=14,
                fontweight='bold',
                pad=20
            )
            
            # Enhance text
            for text in texts:
                text.set_fontsize(11)
                text.set_fontweight('bold')
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontsize(10)
                autotext.set_fontweight('bold')
            
            # Add legend with counts
            legend_labels = [f"{status}: {count}" for status, count in status_counts.items()]
            ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))
            
            plt.tight_layout()
            
            # Save chart
            filename = self.config.get('pie_status', {}).get('filename', 'risk_statuses_pie.png')
            filepath = self.output_folder / filename
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            plt.close()
            
            self._log(f"  Saved: {filepath}")
            return str(filepath)
            
        except Exception as e:
            self._log(f"Error creating status pie chart: {str(e)}", "error")
            return None
    
    def generate_categories_pie_chart(self) -> Optional[str]:
        """
        Generate pie chart: % Split Open Risk Categories
        
        Returns:
            Path to saved chart
        """
        try:
            self._log("Creating pie chart: % Split Open Risk Categories")
            
            # Filter for open risks only
            open_risks = self.data[self.data['Status'] == 'Open'].copy()
            
            if open_risks.empty:
                self._log("No open risks found for categories pie chart", "warning")
                return None
            
            # Count risks by category
            category_counts = open_risks['Category'].value_counts()
            
            # Create pie chart
            fig, ax = plt.subplots(
                figsize=(
                    self.config.get('pie_categories', {}).get('width', 8),
                    self.config.get('pie_categories', {}).get('height', 6)
                )
            )
            
            # Define colors for categories
            category_colors = {
                'Resources': '#e91e63',
                'Cyber': '#9c27b0',
                'Stability': '#3f51b5',
                'Delivery': '#00bcd4',
                'Budget': '#4caf50',
                '3rd Party': '#ff9800'
            }
            pie_colors = [category_colors.get(cat, '#808080') for cat in category_counts.index]
            
            wedges, texts, autotexts = ax.pie(
                category_counts.values,
                labels=category_counts.index,
                autopct='%1.1f%%',
                startangle=90,
                colors=pie_colors,
                explode=[0.03] * len(category_counts)  # Slight separation
            )
            
            # Formatting
            ax.set_title(
                self.config.get('pie_categories', {}).get('title', '% Split Open Risk Categories'),
                fontsize=14,
                fontweight='bold',
                pad=20
            )
            
            # Enhance text
            for text in texts:
                text.set_fontsize(10)
                text.set_fontweight('bold')
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontsize=9
                autotext.set_fontweight('bold')
            
            # Add legend with counts
            legend_labels = [f"{cat}: {count}" for cat, count in category_counts.items()]
            ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))
            
            plt.tight_layout()
            
            # Save chart
            filename = self.config.get('pie_categories', {}).get('filename', 'risk_categories_pie.png')
            filepath = self.output_folder / filename
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            plt.close()
            
            self._log(f"  Saved: {filepath}")
            return str(filepath)
            
        except Exception as e:
            self._log(f"Error creating categories pie chart: {str(e)}", "error")
            return None
